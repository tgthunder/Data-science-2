class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    
    def printdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"
    
    @classmethod
    def change_leaves(self,newleaves):
        self.no_of_leaves=newleaves

    def __add__(self,other):
        return self.salary + other.salary

    def __truediv__(self,other):
        return  self.salary / other.salary

    def __mul__(self,other):
        return self.salary * other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
         return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"
        
emp1=Employee("Sudarshan",345,"Programmer")
emp2=Employee("Rohan",45,"Cleaner")

print(emp1*emp2)
print(repr(emp1))




