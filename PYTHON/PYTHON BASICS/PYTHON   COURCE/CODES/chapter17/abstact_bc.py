from abc import ABC,abstractclassmethod
# if we define abstract base class we have to define all the functions from base class
# we can not make objects of abstract base classsss
class shape(ABC):
    @abstractclassmethod

    def printarea():
        return 0


class Rectangle(shape):
    type="Rectangle"
    side=4
    def __init__(self):
        self.length=4
        self.breadth=5

    def printarea(self):
        return self.length*self.breadth

rect=Rectangle()
