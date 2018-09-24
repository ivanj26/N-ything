from __future__ import print_function
from pieces import Bishop, Knight, Queen, Rook
from random import choice, random, randint, shuffle

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
				# Push new instance to a list.
				self.get_pieces().append(obj)

	def get_pieces(self):
		"""It gets list of pieces on the board.
		
		Parameters
		----------
		idx : int, optional
			index number (the default is None, which returns all list of pieces)
		
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

	def convert_to_axis(self, val):
		"""It converts grid system to x,y-axis.
		
		Parameters
		----------
		val : int
			grid value
		
		Returns
		-------
		dictionary
			x,y-axis value
		"""

		return {
			'y': val / 8,
			'x': val % 8,
		}

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

	def random_pick(self, shuffle = False):
		"""It picks random object from the list or shuffle list of object.
		
		Parameters
		----------
		shuffle : bool, optional
			Flag for shuffle (the default is False, which is not shuffle the list)
		
		Returns
		-------
		object or list
			If shuffle is False, then it returns a random object from the list.
			Otherwise, it returns a shuffle list of objects.
		"""

		if (not shuffle):
			random_number = random()
			randomize_index_number = round(random_number * (len(self.get_pieces())-1))

			return (self.get_pieces()[int(randomize_index_number)])
		# If shuffle is True.
		return shuffle(self.get_pieces())


	def random_move(self, shuffle = False):
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

		# Converts object position to grid system.
		piece_location = []
		for piece in (self.get_pieces()):
			piece_location.append(self.convert_to_grid(piece.get_x(), piece.get_y()))
		# Get maximum grid.
		max_grid = self.convert_to_grid(self.get_max_columns()-1, self.get_max_rows()-1)
		if (not shuffle):
			# Choose random grid value except piece locations.
			random_grid = choice([i for i in range(0, max_grid) if i not in piece_location])

			return self.convert_to_axis(random_grid)
		# Shuffle the possible moves, when the shuffle is True.
		possible_grid = shuffle([i for i in range(0, max_grid) if i not in piece_location])
		possible_moves = []
		for val in possible_grid:
			possible_moves.append(self.convert_to_axis(val))
		
		return possible_moves

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

		for y in range(self.get_max_rows()-1, -1, -1):
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
			print (str(piece) + ' (', self.convert_to_grid(piece.get_x(), piece.get_y()) , ')')