from pieces import *

class Board:
	def __init__(self, request):
		"""Method contructor.

	    Parameters
	    ----------
	    request : dictionary
	        Dictionary of the total ChessPiece to be instantiate.

	    Returns
	    -------
		    returns nothing

	    """

		self.__MAX_ROW = 8
		self.__MAX_COLUMN = 8
		self.__list_of_pieces = []
		for (key, value) in (request.items()):
			print(key, value)

	def is_out_of_bound(self, chessPiece):
		"""Method to check whether the chessPiece position is out of board index.

		Parameters
		----------
		chessPiece : object
		    Instance of ChessPiece.

		Returns
		-------
		boolean
		    True if the position is out of bound, otherwise false.

		"""

		return ((chessPiece.get_x()<0 or chessPiece.get_x()>self.__MAX_ROW) or
		(chessPiece.get_y()<0 or chessPiece.get_y()>self.__MAX_COLUMN))

	def is_move_valid(self, position):
		"""Short summary.

		Parameters
		----------
		position : type
		    Description of parameter `position`.

		Returns
		-------
		type
		    Description of returned object.

		"""
		return

	def random_pick(self):
		"""Short summary.

		Returns
		-------
		type
		    Description of returned object.

		"""
		random_number = random()
		randomize_index_number = round(random_number * (len(self.__list_of_pieces)-1))
		return (self.__list_of_pieces[randomize_index_number])

	def random_move(self):
		"""Short summary.

		Returns
		-------
		type
		    Description of returned object.

		"""
		return

	def calculate_heuristic(self):
		"""Short summary.

		Returns
		-------
		type
		    Description of returned object.

		"""
		return
