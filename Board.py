from __future__ import print_function
from pieces import Bishop, Knight, Queen, Rook
from random import choice, random, sample, shuffle

class Board:
	def __init__(self, request):
		"""It instantiates board conditions based on request file given.
		
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

		self.__COLORS = []
		self.__MAX_ROWS = 8
		self.__MAX_COLUMNS = 8
		self.__list_of_pieces = []

		# Create new ChessPiece instance based on request.
		for (key, value) in (request.items()):
			# Get color property.
			color = key.split()[0]
			# Get piece type.
			piece_type = key.split()[1]
			# Iterate until total request number of each chess piece type has been created.
			for _ in range (value):
				# Append if new color variant exist.
				if color not in (self.get_colors()):
					self.get_colors().append(color)
				obj = None
				position = self.random_move()
				if (piece_type == 'BISHOP'):
					obj = Bishop(color, position['x'], position['y'])
				elif (piece_type == 'KNIGHT'):
					obj = Knight(color, position['x'], position['y'])
				elif (piece_type == 'QUEEN'):
					obj = Queen(color, position['x'], position['y'])
				elif (piece_type == 'ROOK'):
					obj = Rook(color, position['x'], position['y'])
				# Append new instance to a list.
				self.get_pieces().append(obj)

	def get_colors(self):
		"""It returns a list of chess pieces colors variant.
		
		Returns
		-------
		list
			chess piece colors variant
		"""

		return self.__COLORS

	def get_pieces(self, color = None):
		"""It returns list of pieces on the board.
		
		Parameters
		----------
		color : string, optional
			chess piece color (the default is None, which returns all list of pieces)
		
		Returns
		-------
		list
			list of pieces on the board.
		"""
		if (color == "WHITE"):
			return [piece for piece in self.get_pieces() if piece.get_color() == "WHITE"]
		elif (color == "BLACK"):
			return [piece for piece in self.get_pieces() if piece.get_color() == "BLACK"]
		
		return self.__list_of_pieces

	def get_max_columns(self):
		"""It returns max columns on the board.
		
		Returns
		-------
		int
			max columns on the board.
		"""

		return self.__MAX_COLUMNS

	def get_max_rows(self):
		"""It returns max rows on the board.
		
		Returns
		-------
		int
			max rows on the board.
		"""

		return self.__MAX_ROWS

	@classmethod
	def convert_to_grid(self, x, y):
		"""It converts x,y-axis to grid systems.
		
		Parameters
		----------
		x : int
			x-axis
		y : int
			y-axis
		
		Returns
		-------
		int
			grid value
		"""

		return (y*8 + x)

	@classmethod
	def convert_to_axis(self, value):
		"""It converts grid system to x,y-axis.
		
		Parameters
		----------
		value : int
			grid value
		
		Returns
		-------
		dictionary
			x,y-axis value
		"""

		return {
			'x': value % 8,
			'y': value / 8,
		}

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

	def is_overlap(self, x, y, color):
		"""It returns an integer that indicates the value of x, y position in one of the
		current piece's location.
		
		Parameters
		----------
		x : int
			position of x
		y : int
			position of y
		color : string
			chess piece color
		
		Returns
		-------
		int
			-1: x, y position is not in any of current list of piece's location.
			 0: x, y position is in one of current list of piece's location, but color is different.
			 1: x, y position is in one of current list of piece's location and color is match.
		"""

		for piece in (self.get_pieces()):
			if (piece.get_x() == x) and (piece.get_y() == y):
				if (piece.get_color() == color):
					return 1
				
				return 0
		
		return -1

	def random_pick(self, option = False):
		"""It picks random object from the list or option list of object.
		
		Parameters
		----------
		option : bool, optional
			Flag for option (the default is False, which is not option the list)
		
		Returns
		-------
		object or list
			If option is False, then it returns a random object from the list.
			Otherwise, it returns a option list of objects.
		"""

		if (not option):
			random_number = random()
			randomize_index_number = round(random_number * (len(self.get_pieces())-1))

			return (self.get_pieces()[int(randomize_index_number)])

		return sample(self.get_pieces(), len(self.get_pieces()))

	def random_move(self, option = False):
		"""It gives a random position or a list of a valid position to move.
		
		Parameters
		----------
		option : bool, optional
			Flag (the default is False, which means just give a position)
		
		Returns
		-------
		dictionary or list
			Returns a dictionary of {x, y} when option is False.
			Otherwise, returns list of dictionary of {x, y}.
		"""

		# Converts object position to grid system.
		piece_location = []
		for piece in (self.get_pieces()):
			piece_location.append(self.convert_to_grid(piece.get_x(), piece.get_y()))
		# Get maximum grid.
		max_grid = self.convert_to_grid(self.get_max_columns()-1, self.get_max_rows()-1)
		if (not option):
			# Choose random grid value except piece locations.
			random_grid = choice([i for i in range(0, max_grid) if i not in piece_location])

			return self.convert_to_axis(random_grid)
		# Get all possible grid.
		possible_grid = [i for i in range(0, max_grid) if i not in piece_location]
		# Shuffle the possible moves.
		shuffle(possible_grid)
		possible_moves = []
		# Get all possible moves.
		for val in possible_grid:
			possible_moves.append(self.convert_to_axis(val))
		
		return possible_moves

	def count_attack(self, enemy = False):
		"""It counts how many attack that might be involved within current board's state.

		Foreach pieces on the current list of pieces:
			It checks how many pieces that it can attack based on its rules and colors.
		
		Heuristic value is the sum of how many pieces that each of pieces can attack.
		
		Parameters
		----------
		enemy : bool, optional
			Enemy means attacks between enemies (different color) 
			(the default is False, which is attack within friends)
		
		Returns
		-------
		int
			total of attack that might be involved.
		"""

		# Get colors variant.
		colors = self.get_colors()[:]
		# Set initiate value.
		value = 0

		# Calculate attack within friends.
		for color in colors:
			if (enemy) :
				if (color == 'WHITE'):
					opponent_color = 'BLACK'
				else:
					opponent_color = 'WHITE'
			else:
				opponent_color = color
			for piece in (self.get_pieces(color)):
				for rule in (piece.get_rules()):
					if isinstance(piece, Knight):
						current_move = rule()
						if (not self.is_out_of_bound(current_move['x'], current_move['y'])):
							inc = self.is_overlap(current_move['x'], current_move['y'], opponent_color)
							if (inc != -1):
								value += inc
					else:
						i = 1
						current_move = rule(i)
						while (not self.is_out_of_bound(current_move['x'], current_move['y'])):
							inc = self.is_overlap(current_move['x'], current_move['y'], opponent_color)
							if (inc != -1):
								value += inc
								break
							i += 1
							current_move = rule(i)
		return value

	def calculate_heuristic(self):
		"""It calculates the heuristic value of current board's state.
		
		Returns
		-------
		dictionary
			a: total attacks within the same color.
			b: total attacks across different color.
			total: sum of b - a, it is used for total heuristic value.
		"""

		a = self.count_attack(False)
		if (len(self.get_colors()) == 1):
			b = 0
		else:
			b = self.count_attack(True)

		return {
			'a': a,
			'b': b,
			'total': b - a,
		}

	def draw(self):
		"""It draws location of current board.
		
		"""

		for y in range(self.get_max_rows()-1, -1, -1):
			print(str(y) + ' ', end='')
			for x in range(self.get_max_columns()):
				found = False
				for piece in (self.get_pieces()):
					if (piece.get_x() == x and piece.get_y() == y):
						found = True
						break
				if found:
					if (piece.get_color() == "BLACK"):	
						print(' ' + piece.__class__.__name__[0].lower() + ' ', end='')
					else:
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
	
	def set_pieces(self, pieces):
		self.__list_of_pieces = pieces