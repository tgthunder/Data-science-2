#26. Write a program to calculate the total area of multiple rectangles using a class `Rectangle`.

class Rectangle(object):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"Area of rectangle: {self.length*self.breadth}"
    
    def __add__(self):
        pass
    
    
r1 = Rectangle(10,23)
r2 = Rectangle(34,10)

print(r1.area())