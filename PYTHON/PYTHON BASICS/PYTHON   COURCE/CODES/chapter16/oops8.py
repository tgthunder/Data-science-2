# Multiple inheritance


class Employee:
    no_of_leaves=10
    var=8
    def __init__(self,aname,asalary,atask):
        self.name=aname
        self.salary=asalary
        self.task=atask

    @classmethod
    def change_leaves(self, newleaves):
        self.no_of_leaves=newleaves

    @staticmethod
    def printgood(string):
        return f"This is good {string}"

        
        
sudarshan=Employee("Sudarshan",34500,"Investor")
sourabh=Employee("sourabh",5000,"Manager")

class Player:
    no_of_games=5
    var=9
    def __init__(self,name,game):
        self.name=name
        self.game=game
    
    def printdetails(self):
        return f"This is {self.name} and game is {self.game}"
Manoj=Player("Manoj","Cricket")
print(Manoj.printdetails())

class Coolprogrammer(Employee,Player): #this class take Employee 1st as constuctor
# If you change the order of class it will change the constructor of inherit class
    languages="C++"
    
    def language(self):
        return self.languages
Abhijit=Coolprogrammer("Abhijit",1000,"Coolprogrammer")
print(Abhijit.salary)

det=Abhijit.language()
print(det)
print(Abhijit.var)
