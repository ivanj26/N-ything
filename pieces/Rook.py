from ChessPiece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, color, x, y):
        """This method initiliaze Rook's attributes and rules.

        Parameters
        ----------
        color : string
            Color of Rook.
        x : int
            Location x of Rook.
        y : int
            Location y of Rook.

        Returns
        -------
            returns nothing.

        """

        super(Rook, self).__init__(color, x, y)
        self.__name = "R"
        self.__rules = [lambda i : {'x' : self.get_x() + i, 'y' : self.get_y()}, lambda i : {'x' : self.get_x() - i, 'y' : self.get_y()},
                      lambda i : {'x' : self.get_x(), 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x(), 'y' : self.get_y() - i}]

    def get_rules(self):
        """Gets set of rule in Rook.

        Returns
        -------
        list of dictionary
            returns list of rule.

        """
        return self.__rules

    def __str__(self):
        """Gets name of class.

        Returns
        -------
        string
            returns name of class.

        """
        return self.__name
