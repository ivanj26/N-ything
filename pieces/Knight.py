from ChessPiece import ChessPiece

class Knight(ChessPiece):
    def __init__(self, color, x, y):
        """This method initiliaze Knight's attributes and rules.

        Parameters
        ----------
        color : string
            Color of Knight.
        x : int
            Location x of Knight.
        y : int
            Location y of Knight.

        Returns
        -------
            returns nothing.

        """

        super(Knight, self).__init__(color, x, y)
        self.__name = "K"
        self.__rules = [lambda : {'x' : self.get_x() - 2, 'y' : self.get_y() + 1}, lambda : {'x' : self.get_x() - 1, 'y' : self.get_y() + 2},
                      lambda : {'x' : self.get_x() + 1, 'y' : self.get_y() + 2}, lambda : {'x' : self.get_x() + 2, 'y' : self.get_y() + 1},
                      lambda : {'x' : self.get_x() + 2, 'y' : self.get_y() - 1}, lambda : {'x' : self.get_x() + 1, 'y' : self.get_y() - 2},
                      lambda : {'x' : self.get_x() - 1, 'y' : self.get_y() - 2}, lambda : {'x' : self.get_x() - 2, 'y' : self.get_y() - 1}]

    def get_rules(self):
        """Gets set of rule in Knight.

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
