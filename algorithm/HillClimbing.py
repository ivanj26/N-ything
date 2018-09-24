from __future__ import print_function
import os, sys
sys.path.append('../')
sys.path.append('../pieces')
from Board import Board
from random import randint
from time import sleep, time
from pieces import Bishop, Knight, Queen, Rook

class HillClimbing:
	def __init__(self, request, option, max_attempts):
		"""Instantiate hill climbing algorithm.
		
		Parameters
		----------
		request : dictionary
			list of object to be created.
		option : int
			mark which algorithm type should be used.
		max_attempts : int
			number of max restart.
		"""

		self.__REQUEST = request
		self.__MAX_ATTEMPTS = max_attempts
		# If option is 1 then use first choice hill climbing, otherwise stochastic.
		if (option == 1):
			self.first_choice()
		self.stochastic()
	
	def get_request(self):
		"""It gets request from file.
		
		Returns
		-------
		dictionary
			list of objects that need to be created.
		"""

		return self.__REQUEST

	def get_max_attempt(self):
		"""It gets max_attempts param.
		
		Returns
		-------
		int
			number of max attempts.
		"""

		return self.__MAX_ATTEMPTS

	def first_choice(self):
		"""First Choice Hill Climbing.

			Workflow:
			1. Pick one of the chess piece to be moved.
			2. Get random location that is possible to move, then calculate its heuristic.
			3. If it is better than current heuristic, then accept it. Otherwise, repeat step 2.
			4. If goals achived, then exit.
			5. If there is no possible better move, then repeat step 1.
			6. If all pieces do not have any better move, then it stucks to local maxima.
			7. Restart initial state, if necessary.

		"""

		# Start iteration.
		attempts = 1
		start = round(time(), 3)

		# Loop until max attempts are reached.
		while (attempts <= self.get_max_attempt()):
			print("Attempts\t= " + str(attempts))
			# Create board object.
			board = Board(self.get_request())
			# Calculate current heuristic.
			current_heuristic = board.calculate_heuristic()
			# Define local maxima.
			local_maxima = False
			# Loop until goal heuristic and local maxima is reached.
			while ((current_heuristic > 0) and (not local_maxima)):
				# Get piece queue.
				piece_queue = board.random_pick(True)
				# Better state is defined as the heuristic is better than current heuristic.
				better_state = False
				# Loop until all pieces has gotten turn or there is a better state.
				while ((len(piece_queue) > 0) and (not better_state)):
					# Get one piece to get turn.
					current_piece = piece_queue.pop()
					# Original position
					original_position =  {
						'y': current_piece.get_y(),
						'x': current_piece.get_x(),
					}
					# Get list of all possible moves.
					possible_moves = board.random_move(True)
					# Loop until no other possible move for current piece.
					while (len(possible_moves) > 0):
						# Get a position to move.
						current_move = possible_moves.pop()
						# Replace current position of piece with current move.
						current_piece.set_x(current_move['x'])
						current_piece.set_y(current_move['y'])
						# Calculate heuristic after change to new position.
						heuristic = board.calculate_heuristic()
						# Accept proposed move, if heuristic is better than current heuristic.
						if (heuristic < current_heuristic):
							current_heuristic = heuristic
							better_state = True
							break
						else:
							#Restore the position of piece, not accept the changes
							current_piece.set_x(original_position['x'])
							current_piece.set_y(original_position['y'])
				# Local maxima has reached because there is no possible piece moves,
				# that gives a better heuristic.
				if (not better_state):
					local_maxima = True
			# Goal has reached.
			if (current_heuristic == 0):
				finish = round(time(), 3)
				os.system('clear')
				print("Yeay, solution found after", attempts, "attempt(s)!")
				print("Elapsed time = " + str(finish-start) + " seconds\n")
				board.draw()
				print("  ", str(board.calculate_heuristic()), " 0")
				return

			# Restart attempt.
			attempts += 1
			sleep(0.03)
			os.system('clear')

		# Maximum attempts reached.
		finish = round(time(), 3)
		os.system('clear')
		print("Unfortunately, solution not found after", attempts-1, "attempt(s)!")
		print("This might be because you've exceeded the maximum attempts.")
		print("Elapsed time = " + str(finish-start) + " seconds\n")
		board.draw()
		print("  ", str(board.calculate_heuristic()), " 0")
		return

	def stochastic(self):
		"""Stochastic Hill Climbing
		
			Workflow:
			1. Pick one of the chess piece to be moved.
			2. Calculate heuristic in each of its possible moves.
			3. Get random location that gives better heuristic value.
			4. If goals achived, then exit.
			5. If there is no possible better move, then repeat step 1.
			6. If all pieces do not have any better move, then it stucks to local maxima.
			7. Restart initial state, if necessary.

		"""
		# Start iteration.
		attempts = 1
		start = round(time(), 3)

		# Loop until max attempts are reached.
		while (attempts <= self.get_max_attempt()):
			print("Attempts\t= " + str(attempts))
			# Create board object.
			board = Board(self.get_request())
			# Calculate current heuristic.
			current_heuristic = board.calculate_heuristic()
			# Define local maxima.
			local_maxima = False
			# Loop until goal heuristic and local maxima is reached.
			while ((current_heuristic > 0) and (not local_maxima)):
				# Get piece queue.
				piece_queue = board.random_pick(True)
				# Better state is defined as the heuristic is better than current heuristic.
				better_states = []
				# Loop until all pieces has gotten turn or there is a list of better states.
				while ((len(piece_queue) > 0) and (len(better_states) == 0)):
					# Get one piece to get turn.
					current_piece = piece_queue.pop()
					# Original position
					original_position =  {
						'y': current_piece.get_y(),
						'x': current_piece.get_x(),
					}
					# Get list of all possible moves.
					possible_moves = board.random_move(True)
					# Loop until no other possible move for current piece.
					while (len(possible_moves) > 0):
						# Get a position to move.
						current_move = possible_moves.pop()
						# Replace current position of piece with current move.
						current_piece.set_x(current_move['x'])
						current_piece.set_y(current_move['y'])
						# Calculate heuristic after change to new position.
						heuristic = board.calculate_heuristic()
						# Accept proposed move, if heuristic is better than current heuristic.
						if (heuristic < current_heuristic):
							# Add to list of better_states
							better_states.append(current_move)
						#Restore the position of piece, not accept the changes
						current_piece.set_x(original_position['x'])
						current_piece.set_y(original_position['y'])
					# There is/are better states, then choose randomly.
					if (len(better_states) > 0):
						idx = randint(0, len(better_states)-1)
						chosen_move = better_states[idx]
						# Replace current position of piece with chosen move.
						current_piece.set_x(chosen_move['x'])
						current_piece.set_y(chosen_move['y'])
						# Calculate heuristic after change to new position.
						heuristic = board.calculate_heuristic()
						current_heuristic = heuristic
				# Local maxima has reached because there is no possible piece moves,
				# that gives a better heuristic.
				if (len(better_states) == 0):
					local_maxima = True
			# Goal has reached.
			if (current_heuristic == 0):
				finish = round(time(), 3)
				os.system('clear')
				print("Yeay, solution found after", attempts, "attempt(s)!")
				print("Elapsed time = " + str(finish-start) + " seconds\n")
				board.draw()
				print("  ", str(board.calculate_heuristic()), " 0")
				return

			# Restart attempt.
			attempts += 1
			sleep(0.03)
			os.system('clear')

		# Maximum attempts reached.
		finish = round(time(), 3)
		os.system('clear')
		print("Unfortunately, solution not found after", attempts-1, "attempt(s)!")
		print("This might be because you've exceeded the maximum attempts.")
		print("Elapsed time = " + str(finish-start) + " seconds\n")
		board.draw()
		print("  ", str(board.calculate_heuristic()), " 0")
		return