# Public
# Protected (_)
# Private (__)
class Employee:
    no_of_leaves=10

    _protect=12
    __priv=14      #(for private python will do name mangling for protection use __classname__privat)
    def __init__(self,aname,asalary,atask):
        self.name=aname
        self.salary=asalary
        self.task=atask
    @classmethod
    def change_leaves(self, newleaves):
        self.no_of_leaves=newleaves
    @classmethod
    def from_dash(self, string):
        # params=string.split("-")
        # print(params)
        # return self(params[0],params[1],params[2])
        return self(*string.split("-"))

        
sudarshan=Employee("Sudarshan",34500,"Investor")
sourabh=Employee("sourabh",5000,"Manager")
Karan=Employee.from_dash("karan-4000-Helper")
emp=Employee("Harry",344,"Employee")
print(emp._protect)
print(emp._Employee__priv) 