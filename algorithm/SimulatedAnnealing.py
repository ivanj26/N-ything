from __future__ import print_function
from time import sleep
from time import time
from copy import copy
import os
import sys
import math
sys.path.append('../')
sys.path.append('../pieces')

from random import random
from pieces import ChessPiece
from Board import Board

class SimulatedAnnealing:
    def __init__(self, request, max_attempt, cooling_rate, temp):
        """This constructs SimulatedAnnealing instance and create Board object.

        Parameters
        ----------
        request : dictionary
            Dictionary of list of piece.

        Returns
        -------
        nothing
        """
        self.__TEMP = temp
        self.__COOLING_RATE = cooling_rate
        self.__MAX_ATTEMPTS = max_attempt

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

    def boltzman_dist(self, e, e1, temp):
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
        return math.exp((e1 - e) / temp)

    def start(self):
        """This method performs simulated annealing algorithm.
        Returns
        -------
        void
        """
        attempts = 1
        colors = len(self.__board.get_colors())

        best = None
        best_board = None

        if (colors > 1):
            best = {'a' : 0, 'b' : -999 ,'total': -999}
        else:
            best = {'a' : 999, 'b' : 0, 'total': -999}

        #Calculate current heuristic
        current_heuristic = self.__board.calculate_heuristic()

        #Start
        start = round(time(), 3)

        while (attempts < self.__MAX_ATTEMPTS):
            #Initialize temperature
            temp = self.__TEMP
            print("Attempts\t= " + str(attempts))

            #when temp < 1 -> prob nearly to zero
            while (temp > 1 and current_heuristic['total'] != 0):
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

                if (current_heuristic['total'] < heuristic['total']):
                    #Absolutely accept the changes, get maximum heuristic
                    current_heuristic = heuristic
                else:
                    probability = self.boltzman_dist(current_heuristic['total'], heuristic['total'], temp)
                    if (random() <= probability):
                        #Accept the changes
                        current_heuristic = heuristic
                    else:
                        #Restore the position of piece, not accept the changes
                        piece.set_x(old_position['x'])
                        piece.set_y(old_position['y'])

                    temp = self.cooling_down(temp)

            #Check if current heuristic is better than current best
            if (best['total'] < current_heuristic['total']):
                best = current_heuristic
                best_board = copy(self.__board)

            #For count(color) = 1, returns answer if current_heuristic equals to zero
            if (current_heuristic['total'] == 0 and colors == 1):
                finish = round(time(), 3)
                os.system('clear')
                print("Yeay, solution found after", str(attempts), "attempt(s)!")
                print("Elapsed time = " + str(finish-start) + " seconds\n")
                self.__board.draw()
                print("  ", str(current_heuristic['a']), '', str(current_heuristic['b']))
                return

            #Restart by reinitialize the board
            self.__board = Board(self.__request)

            #Calculate current heuristic
            current_heuristic = self.__board.calculate_heuristic()

            #Increment the attempts
            attempts+=1
            sleep(0.03)
            os.system('clear')

        #Maximum attempts reached
        finish = round(time(), 3)

        os.system('clear')

        print("S.A Algorithm approximates global optimum (with ", attempts, " attempts)")
        print("Elapsed time = " + str(finish - start) + " seconds\n")

        #Draw best Board
        if (current_heuristic['total'] < best):
            best_board.draw()
            print(" ", best['a'] , " ", best['b'])
        else:
            self.__board.draw()
            print(" ", str(current_heuristic['a']) , " ", str(current_heuristic['b']))

        return
