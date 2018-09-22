from ChessPiece import ChessPiece

class Queen(ChessPiece):
    def __init__(self, color, x, y):
        """This method initiliaze Queen's attributes and rules.

        Parameters
        ----------
        color : string
            Color of Queen.
        x : int
            Location x of Queen.
        y : int
            Location y of Queen.

        Returns
        -------
            returns nothing.

        """

        super(Queen, self).__init__(color, x, y)
        self.__name = "Q"
        self.__rules = [lambda i : {'x' : self.get_x() + i, 'y' : self.get_y()}, lambda i : {'x' : self.get_x() - i, 'y' : self.get_y()},
                      lambda i : {'x' : self.get_x(), 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x(), 'y' : self.get_y() - i},
                      lambda i : {'x' : self.get_x() + i, 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x() + i, 'y' : self.get_y() - i},
                      lambda i : {'x' : self.get_x() - i, 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x()  - i, 'y' : self.get_y() - i}]

    def get_rules(self):
        """Gets set of rule in Queen.

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
