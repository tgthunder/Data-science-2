class Employee:
    no_of_leaves=10
    def __init__(self,aname,asalary,atask):
        self.name=aname
        self.salary=asalary
        self.task=atask

    @classmethod
    def change_leaves(self, newleaves):
        self.no_of_leaves=newleaves

    @staticmethod
    def printgood(string):
        return f"This is good {string}"

        
        
sudarshan=Employee("Sudarshan",34500,"Investor")
sourabh=Employee("sourabh",5000,"Manager")
print(sourabh.printgood("sourabh"))