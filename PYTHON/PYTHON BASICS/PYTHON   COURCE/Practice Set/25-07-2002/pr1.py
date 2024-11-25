class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f'name is {self.name} and salary is {self.salary} and role is {self.role}'

sudarshan=Employee("Sudarshan",50000,"Owner")

sourabh=Employee("Sourabh",40000,"Manger")

# sourabh.name="Sourbh"
# sourabh.salary=40000
# sourabh.role="Manager"

# sudarshan.name="Sudarshan"
# sudarshan.salary=50000
# sudarshan.role="Owner"


# print(sudarshan.name)
# print(sourabh.no_of_leaves)
# print(sudarshan.printdetails())

print(sudarshan.name)
print(sourabh.salary)

