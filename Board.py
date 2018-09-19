# from pieces.Bishop import Bishop
# from pieces.Knight import Knight
# from pieces.Queen import Queen
# from pieces.Rook import Rook

class Board:
	"""
	Method contructor.
	@param request is dictionary of the total ChessPiece to be instantiate.
	"""
	def __init__(self, request):
		self.__MAX_ROW = 8
		self.__MAX_COLUMN = 8
		self.__list_of_pieces = []
		for (key, value) in (request.items()):
			print(key, value)

	"""
	Method to check whether the chessPiece position is out of board index.
	@return boolean true if the position is out of bound, otherwise false.
	"""
	def is_out_of_bound(self, chessPiece):
		return(
			(chessPiece.get_x()<0 or chessPiece.get_x()>self.__MAX_ROW)
			or (chessPiece.get_y()<0 or chessPiece.get_y()>self.__MAX_COLUMN)
		)

	def is_move_valid(self):
		return

	def random_pick(self):
		random_number = random()
		randomize_index_number = round(random_number * (len(self.__list_of_pieces)-1))
		return (self.__list_of_pieces[randomize_index_number])

	def random_move(self):
		return

	def calculate_heuristic(self):
		return
