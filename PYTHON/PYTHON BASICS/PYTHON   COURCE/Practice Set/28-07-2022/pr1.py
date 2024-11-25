class Employee:
    no_of_leaves=10

    def __init__(self,name,salary,role):
            self.name=name
            self.salary=salary
            self.role=role

    def printdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @staticmethod
    def divison(a,b):
        return a/b

sudarshan=Employee("Sudarshan",250,"Owner")
sourabh=Employee("Sourabh",100,"Manager")

print(sourabh.salary)

print(sudarshan.printdetails())

print(sudarshan)
print(sourabh.__dict__)
print(id(sudarshan))

sudarshan.change_leaves(23)
print(sourabh.no_of_leaves)
print(Employee.no_of_leaves)
