from __future__ import print_function
from pieces import *
from random import randint, random
import string

class Board:
	def __init__(self, request):
		"""This function initiates board conditions based on request file given.
		
		Parameters
		----------
		request : dictionary
			Example of request:
			{
				WHITE ROOK: 2
			}
			It will instantiate two ROOK with property of color WHITE and
			located randomly without any overlapping position.
		
		"""

		self.__MAX_ROWS = 8
		self.__MAX_COLUMNS = 8
		self.__list_of_pieces = []

		# Create new ChessPiece instance based on request.
		for (key, value) in (request.items()):
			color = key.split()[0]
			piece_type = key.split()[1]
			for i in range (value):
				position = self.random_move()

				obj = None
				if (piece_type == 'BISHOP'):
					obj = Bishop(color, position['x'], position['y'])
				elif (piece_type == 'KNIGHT'):
					obj = Knight(color, position['x'], position['y'])
				elif (piece_type == 'QUEEN'):
					obj = Queen(color, position['x'], position['y'])
				elif (piece_type == 'ROOK'):
					obj = Rook(color, position['x'], position['y'])

				self.get_pieces().append(obj)

	def get_pieces(self):
		"""It gets list of pieces on the board.
		
		Returns
		-------
		list
			list of pieces on the board.
		"""

		return self.__list_of_pieces

	def get_max_columns(self):
		"""It gets max columns on the board.
		
		Returns
		-------
		int
			max columns on the board.
		"""

		return self.__MAX_COLUMNS

	def get_max_rows(self):
		"""It gets max rows on the board.
		
		Returns
		-------
		int
			max rows on the board.
		"""

		return self.__MAX_ROWS

	def is_move_valid(self, x, y):
		"""It validates whether the location x,y in the params is valid on the board.
		
		It checks whether the given position is NOT of out of bound and NOT overlapping
		with other piece on the board.

		Parameters
		----------
		x : int
			position of x
		y : int
			position of y
		
		Returns
		-------
		bool
			returns True if the x,y is valid, otherwise False.
		"""

		return (not(self.is_out_of_bound(x, y)) and not(self.is_overlap(x, y)))

	def is_out_of_bound(self, x, y):
		"""It validates x,y position whether the location is within the board boundaries.
		
		Parameters
		----------
		x : int
			position of x
		y : int
			position of y
		
		Returns
		-------
		bool
			returns True if the position is out of board boundaries, otherwise False.
		"""	

		return ((x < 0 or x >= self.get_max_rows()) or (y < 0 or y >= self.get_max_columns()))

	def is_overlap(self, x, y):
		"""It validates whether given x, y position is one of the current piece's location.
		
		Parameters
		----------
		x : int
			position of x
		y : int
			position of y
		
		Returns
		-------
		bool
			returns True if x, y position is one of the current piece's location on the board,
			otherwise False.
		"""

		for piece in self.get_pieces() :
			if (piece.get_x() == x) and (piece.get_y() == y):
				return True
		return False

	def random_pick(self):
		"""It picks random piece on the current list of pieces on the board.
		
		Returns
		-------
		ChessPiece object
			One of ChessPiece object in the current list of pieces.
		"""

		random_number = random()
		randomize_index_number = round(random_number * (len(self.get_pieces())-1))
		return (self.get_pieces()[int(randomize_index_number)])

	def random_move(self):
		"""It gives a position x, y that is valid to move based on is_move_valid.
		
		Returns
		-------
		dictionary
			example of return:
			{
				'x': 1,
				'y': 2,
			}
		"""

		valid = False
		while not valid:
			x = randint(0, 7)
			y = randint(0, 7)
			valid = self.is_move_valid(x, y)

		return {
			'x': x,
			'y': y,
		}

	def calculate_heuristic(self):
		"""It calculates the heuristic value of current pieces locations.

		Foreach pieces on the current list of pieces:
			It checks how many pieces that it can attack based on its rules.
		Heuristic value is the sum of how many pieces that each of pieces can attack.
		
		Returns
		-------
		int
			heuristic value
		"""

		value = 0
		for piece in (self.get_pieces()):
			for rule in (piece.get_rules()):
				if isinstance(piece, Knight):
					current_move = rule()
					if (not self.is_out_of_bound(current_move['x'], current_move['y'])):
						if (self.is_overlap(current_move['x'], current_move['y'])):
							value += 1
							break
				else:
					i = 1
					current_move = rule(i)
					while (not self.is_out_of_bound(current_move['x'], current_move['y'])):
						if (self.is_overlap(current_move['x'], current_move['y'])):
							value += 1
							break
						i+=1
						current_move = rule(i)

		return value

	def draw(self):
		"""It draws location of current board.
		
		"""

		for y in range(self.get_max_rows()):
			print(str(y) + ' ', end='')
			for x in range(self.get_max_columns()):
				found = False
				for piece in (self.get_pieces()):
					if (piece.get_x() == x and piece.get_y() == y):
						found = True
						break
				if found:
					print(' ' + piece.__class__.__name__[0] + ' ', end='')
				else:
					print(' - ', end='')
			print()

		print("  ", end="")
		for x in range(self.get_max_columns()):
			print(' ' + str(x), end=' ')

		print('\n')

	def print_all_pieces(self):
		"""It prints all the pieces locations.
		
		"""

		for piece in (self.get_pieces()):
			print (str(piece) + ' (', piece.get_x(), ', ', piece.get_y(), ')')
