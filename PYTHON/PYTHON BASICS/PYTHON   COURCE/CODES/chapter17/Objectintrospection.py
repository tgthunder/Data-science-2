# object introspection means knowing all the information of that particular object
class Employee():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname} {self.lname} @Codewithharry.com"

    def explain(self):
        return f"This is {self.fname} {self.lname}"
    @property
    def email(self):

        if self.fname==None or self.lname==None:
            print("Email is not set. Please set using setter")

        return f"{self.fname} {self.lname} @Codewithharry.com"

    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee("Skill","F")
print(skillf.email)
print(id(skillf))
print(type("THis is string"))
a="This is a python code"
# print(dir(a))
# print(dir(skillf))

import inspect

print(inspect.getmembers(skillf))