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

sourabh.change_leaves(34)
print(sourabh.no_of_leaves)
print(karan.salary)
print(sudarshan.static("hi I am a python developer"))