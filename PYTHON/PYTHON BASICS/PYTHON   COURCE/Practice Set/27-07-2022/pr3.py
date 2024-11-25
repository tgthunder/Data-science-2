


# Public
# private
# protected
class Employee:
    no_of_leaves=8
    # var=10
    public=20
    _protected=56
    __private=80
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

print(f"The public variable is {sudarshan.public} and the protected variable is {sudarshan._protected}")

print(f"The private varible is {sudarshan._Employee__private}")