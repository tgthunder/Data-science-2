class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    
    def printdetails(self):
        return f'name is {self.name} and salary is {self.salary} and role is {self.role}'

sudarshan=Employee("Sudarshan",50000,"Owner")

sourabh=Employee("Sourabh",40000,"Manger")

sourabh.change_leaves(34)
print(sourabh.no_of_leaves)