from ChessPiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color, x, y):
        """This method initiliaze Bishop's attributes and rules.

        Parameters
        ----------
        color : string
            Color of Bishop.
        x : int
            Location x of Bishop.
        y : int
            Location y of Bishop.

        Returns
        -------
            returns nothing.

        """

        super(Bishop, self).__init__(color, x, y)
        self.__name = "B"
        self.__rules = [lambda i : {'x' : self.get_x() + i, 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x() + i, 'y' : self.get_y() - i},
                        lambda i : {'x' : self.get_x() - i, 'y' : self.get_y() + i}, lambda i : {'x' : self.get_x()  - i, 'y' : self.get_y() - i}]

    def get_rules(self):
        """Gets set of rule in Bishop.

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
