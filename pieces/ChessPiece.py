class ChessPiece:
    def __init__(self, color, x, y):
        """This method initiliaze chess piece attributes (color and position).

        Parameters
        ----------
        color : string
            Color of chess piece.
        x : int
            Location x of chess piece.
        y : int
            Location y of chess piece.

        Returns
        -------
            returns nothing.

        """
        #Declare dictionary of position
        self.__position = {}

        #Set the values
        self.__position['x'] = x
        self.__position['y'] = y
        self.__color = color

    def set_color(self, color):
        """Sets the color of chess piece.

        Parameters
        ----------
        color : string
            Color of chess piece.

        """
        self.__color = color

    def get_color(self):
        """Gets the color of chess piece.

        Returns
        -------
        string
            returns color of chess piece.

        """
        return self.__color

    def set_x(self, x):
        """Sets the x-location of chess piece.

        Parameters
        ----------
        x : int
            Location x of chess piece.
        """
        self.__position['x'] = x

    def set_y(self, y):
        """Sets the y-location of chess piece.

        Parameters
        ----------
        y : int
            Location y of chess piece.
        """
        self.__position['y'] = y

    def get_x(self):
        """Gets the x-location of chess piece.

        Returns
        -------
        int
            returns x-location of chess piece.

        """
        return self.__position['x']

    def get_y(self):
        """Gets the y-location of chess piece.

        Returns
        -------
        int
            returns y-location of chess piece.

        """
        return self.__position['y']
