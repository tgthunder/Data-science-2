# Abstact BC:-
from abc import *

class Myclass(ABC):
    @abstractmethod
    def calculate(self):
        pass

class sub1(Myclass):
    def calculat(self,x):
        self.x=x
        return f"The square of given no is {self.x*self.x}"
import math  
class sub2(Myclass):
    def calculate(self,x):
        self.x=x
        return f"The suare root of the given no is {math.sqrt(self.x)}"

class sub3(Myclass):
    def calculate(self,x):
        self.x=x
        return f"The cube of given no is {self.x**3}"

obj1=sub1()
print(obj1.calculat(3))

obj2=sub2()
print(obj2.calculate(16))

obj3=sub3()

print(obj3.calculate(5))
