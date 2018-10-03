from __future__ import print_function
from time import sleep
from time import time
from copy import copy, deepcopy
import os
import sys
import math
sys.path.append('../')
sys.path.append('../pieces')

from random import random, randint
from pieces import ChessPiece
from Board import Board

class GeneticAlgorithm:
    def __init__(self, request, mutation_prob, max_attempt, max_generation, max_population):
        self.__request = request
        self.__MUTATION_PROB = mutation_prob
        self.__MAX_ATTEMPTS = max_attempt
        self.__MAX_GENERATION = max_generation
        self.__MAX_POPULATION = max_population
        self.__SUM_COLORS = len(Board(request).get_colors())

        self.assign_population(request)

    def assign_population(self, request):
        self.population = []
        for _ in range(self.__MAX_POPULATION):
            self.population.append(Board(request))

        self.population = self.sort_population(self.population)

    def get_fitness(self, board):
        return board.calculate_heuristic()['total']

    def sort_population(self, population):
        population.sort(key=self.get_fitness, reverse=True)
        return population

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

    def stop_searching(self, board):
        if len(board.get_colors()) == 1:
            return board.calculate_heuristic()['total'] == 0
        else:
            return board.calculate_heuristic()['total'] == 9999 #update soon

    def get_best_pieces(self, population):
        return deepcopy(population)[0].get_pieces()

    def find_solution(self, population):
        generation = 1
        while generation <= self.__MAX_GENERATION:
            # calculate total pair in a population
            total_pair = len(population) if len(population)%2 == 0 else len(population)-1
            new_population = []

            # generate childs
            for i in [el for el in list(range(total_pair)) if el % 2 == 0]:
                new_population = new_population + self.reproduce(population[i], population[i+1])

            # assign population with its childs
            population = new_population
            for board in population:
                if random() < self.__MUTATION_PROB:
                    board = self.mutate(board)

            population = self.sort_population(population)

            if self.stop_searching(population[0]):
                break
            generation = generation + 1
        return population[0]
    
    def draw_solution(self, board):
        board.draw()
        print("  ", str(board.calculate_heuristic()['a']), '', 
            str(board.calculate_heuristic()['b']))

    def start(self): 
        attempt = 1

        best = None
        best_board = None

        if (self.__SUM_COLORS > 1):
			best = {'a' : 0, 'b' : -999 ,'total': -999}
        else:
			best = {'a' : 999, 'b' : 0, 'total': -999}

        start = round(time(), 3)
        while attempt <= self.__MAX_ATTEMPTS:

            print("Attempts\t= " + str(attempt))
            
            temp_solution = self.find_solution(self.population)

            if best['total'] < temp_solution.calculate_heuristic()['total']:
                best = copy(temp_solution.calculate_heuristic())
                best_board = copy(temp_solution)

            if self.stop_searching(best_board):
                break

            attempt = attempt + 1
            self.assign_population(self.__request)
            sleep(0.03)
            os.system('clear')
        finish = round(time(), 3)
        
        os.system('clear')
        print("GA Algorithm approximates global optimum (with ", attempt-1, " attempt(s))")
        print("Elapsed time = " + str(finish-start) + " seconds\n")
        self.draw_solution(best_board)




        


        
