from __future__ import print_function
from time import sleep
from time import time
import os
import sys
import math
sys.path.append('../')
sys.path.append('../pieces')

from random import random
from pieces import ChessPiece
from Board import Board

class SimulatedAnnealing:
    def __init__(self, request):
        """This constructs SimulatedAnnealing instance and create Board object.

        Parameters
        ----------
        request : dictionary
            Dictionary of list of piece.

        Returns
        -------
        nothing
        """
        self.__TEMP = 100
        self.__COOLING_RATE = 0.95
        self.__MAX_ATTEMPTS = 50000

        self.__request = request
        self.__board = Board(request)

    def print_immediately(self, attempts, current_heuristic, temp):
        """This method prints Board UI.

        Parameters
        ----------
        attempts : int
            Current attempts in t.
        current_heuristic : int
            Current heuristic in t.
        temp : int
            Current temperature in t.

        Returns
        -------
        void
            Prints Board UI.
        """
        print("Attempts\t\t= " + str(attempts))
        print("Current Heuristic\t= " + str(current_heuristic))
        print("Current Temperature\t= " + str(temp), end='\n\n')
        self.__board.draw()
        sleep(0.025)
        os.system('clear')

    def cooling_down(self, temp):
        """This method returns temp after cooling down.

        Parameters
        ----------
        temp : int
            Current temperature to cool down.

        Returns
        -------
        int
            returns colder temperature.

        """
        return temp * self.__COOLING_RATE

    def boltzman_dist(self, e1, e, temp):
        """This method performs boltzman distribution where exp(-(loss/temp)).

        Parameters
        ----------
        e1 : int
            Neighbor's heuristic.
        e : int
            Current heuristic.
        temp : int
            Current temperature.

        Returns
        -------
        int
            Probability by boltzman.

        """
        return math.exp((e - e1) / temp)

    def start(self):
        """This method performs simulated annealing algorithm.

        Returns
        -------
        void
        """
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
            self.__board = Board(self.__request)

            #Calculate current heuristic
            current_heuristic = self.__board.calculate_heuristic()

            #Increment the attempts
            attempts+=1
            sleep(0.03)
            os.system('clear')

        finish = round(time(), 3)

        print("Heuristic\t= " + str(self.__board.calculate_heuristic()))
        print("Time\t\t= " + str(finish-start) + " seconds")
        print("You've exceeded the maximum attempts!\n")

        self.__board.draw()
