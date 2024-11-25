# Alternative method for contructor


class Employee:
    no_of_leaves=10
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
print(Karan.task)

