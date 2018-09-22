from pieces import *
from random import randint

class Board:
	def __init__(self, request):
		self.__MAX_ROW = 8
		self.__MAX_COLUMN = 8
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
				self.__list_of_pieces.append(obj)
		print(self.__list_of_pieces)

	def is_out_of_bound(self, x, y):
		return ((x < 0 or x > self.__MAX_ROW) or (y < 0 or y > self.__MAX_COLUMN))

	def is_overlap(self, x, y):
		
		return False

	def is_move_valid(self, x, y):
		return (not(self.is_out_of_bound(x, y)) and not(self.is_overlap(x, y)))

	def random_pick(self):
		random_number = random()
		randomize_index_number = round(random_number * (len(self.__list_of_pieces)-1))

		return (self.__list_of_pieces[randomize_index_number])

	def random_move(self):
		valid = False
		while not valid:
			x = randint(0, 8)
			y = randint(0, 8)
			valid = self.is_move_valid(x, y)

		return {
			'x': x,
			'y': y,
		}

	def calculate_heuristic(self):
		return
