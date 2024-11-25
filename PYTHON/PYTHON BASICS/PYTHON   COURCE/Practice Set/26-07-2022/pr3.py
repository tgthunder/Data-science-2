class Employee:
    no_of_leaves=8
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

sudarshan=Employee("Sudarshan",50000,"Owner")

sourabh=Employee("Sourabh",40000,"Manger")

karan=Employee.from_dash("Karan-30000-Helper")

class programmer(Employee):
    # def __init__(self, name, salary, role,languages):
    #     self.name=name
    #     self.salary=salary
    #     self.role=role
    #     self.languages=languages

    def printprog(self):
        print(f'The name is {self.name} and the salary is {self.salary} and the role is {self.role} and languages are {self.languages}')

shubham=programmer()
# Rohan=programmer()

print(shubham.printdetails())
# Rohan.printprog()