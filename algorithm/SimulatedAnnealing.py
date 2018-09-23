from __future__ import print_function
from time import sleep
from time import time
import os
import sys
import math
sys.path.append('../')
sys.path.append('../pieces')

from random import random
from pieces import *
from Board import Board

class SimulatedAnnealing:
    def __init__(self, board):
        self.__TEMP = 100
        self.__COOLING_RATE = 0.95
        self.__MAX_ATTEMPTS = 50000

        self.__board = board

    def print_immediately(self, attempts, current_heuristic, temp):
        print("Attempts\t\t= " + str(attempts))
        print("Current Heuristic\t= " + str(current_heuristic))
        print("Current Temperature\t= " + str(temp), end='\n\n')
        self.__board.draw()
        sleep(0.025)
        os.system('clear')

    def cooling_down(self, temp):
        return temp * self.__COOLING_RATE

    def boltzman_dist(self, e1, e, temp):
        return math.exp((e - e1) / temp)

    def start(self, request):
        attempts = 1

        #Calculate current heuristic
        current_heuristic = self.__board.calculate_heuristic()

        #Start
        start = round(time(), 3)

        while (attempts < self.__MAX_ATTEMPTS):
            #Initialize temperature
            temp = self.__TEMP
            print("Attempts\t= " + str(attempts))

            #when temp < 1 -> prob nearly to zero
            while (temp > 1 and current_heuristic != 0):
                # For the fastest performance, do not update Board UI
                # self.print_immediately(attempts, current_heuristic, temp);

                #Call random_pick from board
                piece = self.__board.random_pick()

                #Store position of piece (temporer)
                old_position = {'x' : piece.get_x(), 'y' : piece.get_y()}

                #Random position by call random_move function
                rand_position = self.__board.random_move()

                #Replace current position of piece with rand_position
                piece.set_x(rand_position['x'])
                piece.set_y(rand_position['y'])

                #Calculate heuristic after change to new position
                heuristic = self.__board.calculate_heuristic()

                if (current_heuristic > heuristic):
                    #Absolutely accept the changes, get minimum heuristic
                    current_heuristic = heuristic
                else:
                    probability = self.boltzman_dist(heuristic, current_heuristic, temp)
                    if (random() <= probability):
                        #Accept the changes
                        current_heuristic = heuristic
                    else:
                        #Restore the position of piece, not accept the changes
                        piece.set_x(old_position['x'])
                        piece.set_y(old_position['y'])

                    temp = self.cooling_down(temp)

            if (current_heuristic == 0):
                finish = round(time(), 3)
                print("Heuristic\t= " + str(self.__board.calculate_heuristic()))
                print("Time\t\t= " + str(finish-start) + " seconds\n")

                self.__board.draw()
                return

            #Restart by reinitialize the board
            self.__board = Board(request)

            #Calculate current heuristic
            current_heuristic = self.__board.calculate_heuristic()

            #Increment the attempts
            attempts+=1
            sleep(0.03)
            os.system('clear')

        return "You've exceeded the maximum attempts!"


# class A:
#     def __init__(self):
#         self.__number = [1,2,3,4,5]
#
#     def get_pieces(self):
#         return self.__number
#
#     def print_all_pieces(self):
#         for i in self.__number:
#             print(i)
# class B:
#     def __init__(self, a):
#         numbers = a.get_pieces()
#         numbers[2] = 10
#
#         a.print_all_pieces()
#
# a = A()
# b = B(a)
