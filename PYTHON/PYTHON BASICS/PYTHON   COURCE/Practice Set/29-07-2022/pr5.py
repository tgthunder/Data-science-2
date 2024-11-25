


class Employee():

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"The email is {self.fname}{self.lname}@gmail.com"

    def explain(self):
        return f"The name is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.lname==None or self.fname==None:
            return "This email is deleted"
        return f"The email is {self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Set now")
        names=string.split("@")[0]
        
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1] 

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee("Skill","F")

print(skillf.email)

print(type(skillf))
print(type(34))
o="This is a string"
print(type(o))

print(dir(skillf))
print(skillf.__dict__)

print(id(skillf))

import inspect

print(inspect.getmembers(skillf))