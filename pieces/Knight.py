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

        ChessPiece.__init__(self, color, x, y)
        self.__name = "Knight"
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

    def get_name():
        """Gets name of class.

        Returns
        -------
        string
            returns name of class.

        """
        return self.__name

# k = Knight("white", 5 ,6)
# print str(k.get_rules()[0]());
