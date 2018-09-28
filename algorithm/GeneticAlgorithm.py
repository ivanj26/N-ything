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
        self.__MUTATION_PROB = 0.8
        self.__MAX_ATTEMPTS = 1000
        self.__MAX_POPULATION = 50
        self.__SUM_COLORS = len(Board(request).get_colors())
        self.__population = []

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
    
    def reproduce(self, parent1, parent2):
        pieces1 = parent1.get_pieces()
        pieces2 = parent2.get_pieces()

        cross_point = randint(0, len(pieces1)-1)
        
        child1 = pieces1[0:cross_point+1] + pieces2[cross_point:len(pieces1)]
        child2 = pieces2[0:cross_point+1] + pieces1[cross_point:len(pieces1)]
        
        print(len(parent1.get_pieces()))

        parent1.set_pieces(child1)
        parent2.set_pieces(child2)
        
        print(len(parent1.get_pieces()))

        return [parent1, parent2]
        
    def stop_searching(self):
        if len(self.__best_board.get_colors()) == 1:
            return self.__best_board.calculate_heuristic()['total'] == 0
        else:
            return self.__best_board.calculate_heuristic()['total'] == 9999 #update soon
        
    def start(self):
        attempt = 1
        while attempt <= self.__MAX_ATTEMPTS:
            total_pair = len(self.__population) if len(self.__population)%2 == 0 else len(self.__population)-1
            new_population = []
            for i in [el for el in list(range(total_pair)) if el % 2 == 0]:
                new_population = new_population + self.reproduce(self.__population[i], self.__population[i+1])
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

            if self.stop_searching():
                break
            
            attempt = attempt+1

            print("Attempt :", attempt)
            print("Best Heuristic :", self.__best_board.calculate_heuristic()['total'])
        
            self.__best_board.draw()

    


            

                
