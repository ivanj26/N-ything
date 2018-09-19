class ChessPiece:
    def __init__(self, color, x, y):
        #Declare dictionary of position
        self.position = {}

        #Set the values
        self.position['x'] = x
        self.position['y'] = y
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_x(self, x):
        self.position['x'] = x

    def set_y(self, y):
        self.position['y'] = y

    def get_x(self):
        return self.position['x']

    def get_y(self):
        return self.position['y']
