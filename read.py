from copy import deepcopy

class A:
    
    def __init__(self, a1, a2):
        self.__atr1 = a1
        self.__atr2 = a2

    def setA1(self, a1):
        self.__atr1 = a1
    

    def setA2(self, a2):
        self.__atr2 = a2
    
    def getA2(self):
        return self.__atr2

    def getA1(self):
        return self.__atr1

obj1 = A(1, 2)
obj2 = deepcopy(obj1)
obj1.setA1(2)
print(obj2.getA1(), obj1.getA1())