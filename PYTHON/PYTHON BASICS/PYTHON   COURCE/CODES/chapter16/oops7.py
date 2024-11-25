# Inheritance
# inheritance means add more content to the class including old content
#1.single inheritance
# single inheritance means inherite single class
class Employee:
    no_of_leaves=10
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

class Programmer(Employee):
    def __init__(self, aname, asalary, atask,languages):
        self.name=aname
        self.salary=asalary
        self.task=atask
        self.languages=languages


    def printall(self):
        return f"This is {self.name} and salary is {self.salary} and task is {self.task} and the languages are {self.languages}"
    
        
        
sudarshan=Employee("Sudarshan",34500,"Investor")
sourabh=Employee("sourabh",5000,"Manager")

Raj=Programmer("Raj",10000,"Programmer",["python","c++"])
Sujal=Programmer("Sujal",12000,"Programmer",["python","java","kotlin"])

print(Raj.printall())