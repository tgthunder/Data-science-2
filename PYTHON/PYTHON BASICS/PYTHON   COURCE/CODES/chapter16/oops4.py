# Contructor (__init__)
class Employee:
    no_of_leaves=10
    def __init__(self,aname,asalary,atask):
        self.name=aname
        self.salary=asalary
        self.task=atask
    @classmethod
    def change_leaves(self, newleaves):
        self.no_of_leaves=newleaves

sudarshan=Employee("Sudarshan",34500,"Investor")
sourabh=Employee("sourabh",5000,"Manager")


print(sudarshan.salary)
print(sourabh.task)
sudarshan.change_leaves(15)
print(sudarshan.no_of_leaves)
print(Employee.no_of_leaves)