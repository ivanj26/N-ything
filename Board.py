from __future__ import print_function
from pieces import *
from random import randint

class Board:
	def __init__(self, request):
		self.__MAX_ROWS = 8
		self.__MAX_COLUMNS = 8
		self.__list_of_pieces = []
		# Create new ChessPiece instance based on request.
		for (key, value) in (request.items()):
			color = key.split()[0]
			piece_type = key.split()[1]
			for i in range (value):
				position = self.random_move()
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
		return self.__list_of_pieces

	def get_max_columns(self):
		return self.__MAX_COLUMNS
	
	def get_max_rows(self):
		return self.__MAX_ROWS

	def is_out_of_bound(self, x, y):
		return ((x < 0 or x > self.get_max_rows()) or (y < 0 or y > self.get_max_columns()))

	def is_overlap(self, x, y):
		overlap_state = False
		for piece in self.get_pieces() :
			if (piece.get_x() == x) and (piece.get_y() == y):
				overlap_state = True
				break
		return overlap_state

	def is_move_valid(self, x, y):
		return (not(self.is_out_of_bound(x, y)) and not(self.is_overlap(x, y)))

	def random_pick(self):
		random_number = random()
		randomize_index_number = round(random_number * (len(self.get_pieces)-1))

		return (self.get_pieces[randomize_index_number])

	def random_move(self):
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
		value = 0
		for piece in (self.get_pieces()):
			for rule in (piece.get_rules()):
				if isinstance(piece, Knight):
					current_move = rule()
					if (self.is_overlap(current_move['x'], current_move['y'])):
						value += 1
				else:
					i = 1
					valid = True
					while valid:
						current_move = rule(i)
						if (self.is_overlap(current_move['x'], current_move['y'])):
							value += 1
						i += 1
						valid = self.is_move_valid(current_move['x'], current_move['y'])

		return value

	def draw(self):
		for y in range(self.get_max_rows()):
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
		return ''

	def print_all_pieces(self):
		for piece in (self.get_pieces()):
			print (piece.__class__.__name__[0] + ' (', piece.get_x(), ', ', piece.get_y(), ')')
		return ''

		