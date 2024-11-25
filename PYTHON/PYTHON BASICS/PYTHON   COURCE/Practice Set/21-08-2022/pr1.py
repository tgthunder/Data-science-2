from distutils.core import run_setup


class Employee:
    No_of_leaves=10
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary

    @classmethod
    def change_leaves(self,newleaves):
        self.No_of_leaves=newleaves
        return self.No_of_leaves

    @staticmethod
    def Multiplication():
        return 34*5


class Programmer:
    var=45
    def __init__(self,name,language):
        self.name=name
        self.language=language
        # self.address=address
    
    def details(self):
        return f"The name is {self.name} language is {self.language} and the address is {self.address} "
    
    def addlanguage(self,newlanguages):
        self.language=self.language+newlanguages
        return self.language

o1=Programmer('Sudarshan','Python')

print(o1.name)

print(o1.addlanguage('C++'))


