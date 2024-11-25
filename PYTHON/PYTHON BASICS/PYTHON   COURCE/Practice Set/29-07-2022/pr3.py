from abc import ABC,abstractclassmethod



class Shape(ABC):
    def printsum(self):
        return 0
    @abstractclassmethod

    def printarea(self):
        return 0
class Rectangle(Shape):
    
    type="rectangle"
    sides=4

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def printarea(self):

        return self.length*self.breadth

a=Rectangle(23,45)
print(a.printarea())
