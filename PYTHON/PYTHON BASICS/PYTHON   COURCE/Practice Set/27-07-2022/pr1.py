class Employee:
    no_of_leaves=8
    # var=10
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    
    @classmethod
    def change_leaves(self,newleaves):
        self.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        # params = string.split("-")
        return cls(*string.split("-"))

    @staticmethod
    def static(string):
        return string

    def printdetails(self):
        return f'name is {self.name} and salary is {self.salary} and role is {self.role}'


class player:
    no_of_games=5
    var=15
    
    def __init__(self,name,game):
        self.name=name
        self.game=game
    
    def printdetails(self):

        return f'name is {self.name} and game is {self.game}'



sudarshan=Employee("Sudarshan",50000,"Owner")
sourabh=Employee("Sourabh",40000,"Manger")

karan=Employee.from_dash("Karan-30000-Helper")

class coolEmployee(Employee,player):
    # var=45
    language="C"
    
    def printlanguage(self):
        return self.language
    
    @staticmethod
    def multiplication(a,b):
        return a*b
    
shubham=coolEmployee("Shubham",30000,"coolEmployee")

print(shubham.printlanguage())

print(shubham.multiplication(4,56))
print(shubham.var)
print(shubham.no_of_games)

