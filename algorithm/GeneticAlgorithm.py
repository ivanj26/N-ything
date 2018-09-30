from __future__ import print_function
from time import sleep
from time import time
import os
import sys
import math
sys.path.append('../')
sys.path.append('../pieces')

from random import random, randint
from pieces import ChessPiece
from Board import Board

class GeneticAlgorithm:
    def __init__(self, request):
        self.__request = request
        self.__MUTATION_PROB = 0.8
        self.__MAX_ATTEMPTS = 20
        self.__MAX_GENERATION = 1000
        self.__MAX_POPULATION = 16
        self.__SUM_COLORS = len(Board(request).get_colors())
        self.__population = []

        self.assign_population(request)
    
    def assign_population(self, request):
        for _ in range(self.__MAX_POPULATION):
            self.__population.append(Board(request))   
        
        self.sort_population()
        
        self.__best_board = self.__population[0]
    
    def get_fitness(self, board):
        return board.calculate_heuristic()['total']

    def sort_population(self):
        self.__population.sort(key=self.get_fitness, reverse=True)
    
    def mutate(self, board):
        piece = board.random_pick()
        new_pos = board.random_move()
        
        piece.set_x(new_pos['x'])
        piece.set_y(new_pos['y'])
        
        return board

    def solve_overlap(self, grid):
        overlap = True
        while overlap:
            for val in set(grid):
                if grid.count(val) > 1:
                    new_val = randint(0, 63)
                    grid[grid.index(val)] = new_val
            
            if len(set(grid)) == len(grid):
                overlap = False
        return grid

    def reproduce(self, parent1, parent2):
        pieces1 = parent1.get_pieces()
        pieces2 = parent2.get_pieces()

        grid1 = []
        grid2 = []
        for i in range(len(parent1.get_pieces())):
            grid1.append(parent1.convert_to_grid(
                pieces1[i].get_x(),
                pieces1[i].get_y()
            ))
            grid2.append(parent2.convert_to_grid(
                pieces2[i].get_x(),
                pieces2[i].get_y()
            ))        
        
        cross_point = randint(0, len(grid1)-1)

        grid_child1 = grid1[0:cross_point+1] + grid2[cross_point+1:len(grid2)]
        grid_child2 = grid2[0:cross_point+1] + grid1[cross_point+1:len(grid1)]
        grid_child1 = self.solve_overlap(grid_child1)
        grid_child2 = self.solve_overlap(grid_child2)
        
        for i in range(len(pieces1)):
            pieces1[i].set_x(Board.convert_to_axis(grid_child1[i])['x'])
            pieces1[i].set_y(Board.convert_to_axis(grid_child1[i])['y'])

            pieces2[i].set_x(Board.convert_to_axis(grid_child2[i])['x'])
            pieces2[i].set_y(Board.convert_to_axis(grid_child2[i])['y'])
                
        parent1.set_pieces(pieces1)
        parent2.set_pieces(pieces2)
        return [parent1, parent2]
        
    def stop_searching(self):
        if len(self.__best_board.get_colors()) == 1:
            return self.__best_board.calculate_heuristic()['total'] == 0
        else:
            return self.__best_board.calculate_heuristic()['total'] == 9999 #update soon
        
    def start(self):
        attempt = 1
        while attempt < self.__MAX_ATTEMPTS:
            generation = 1
            while generation <= self.__MAX_GENERATION:
                total_pair = len(self.__population) if len(self.__population)%2 == 0 else len(self.__population)-1
                new_population = []

                # print("Before")
                # for board in self.__population:
                #     print("len board :", len(board.get_pieces()))

                for i in [el for el in list(range(total_pair)) if el % 2 == 0]:
                    new_population = new_population + self.reproduce(self.__population[i], self.__population[i+1])

                # print("After")
                # for board in self.__population:
                #     print("len board :", len(board.get_pieces()))


                self.__population = new_population
                for board in self.__population:
                    if random() < self.__MUTATION_PROB:
                        # board.draw()
                        board = self.mutate(board)
                        # board.draw()
                        
                self.sort_population()
                self.__best_board = self.__population[0] if (
                    self.get_fitness(self.__population[0]) > self.get_fitness(self.__best_board)
                ) else self.__best_board

                print("Attempt :", attempt)
                print("Generation :", generation)
                print("Best Heuristic :", self.__best_board.calculate_heuristic()['total'])
                self.__best_board.draw()

                if self.stop_searching():
                    break
                
                generation = generation + 1

            self.assign_population(self.__request)
            attempt = attempt + 1


                

    


            

                
