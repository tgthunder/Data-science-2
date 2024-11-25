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


sudarshan=Employee("Sudarshan","Sutar")
sourabh=Employee("Sourabh","Sutar")

print(sudarshan.explain())
print(sudarshan.email)

sudarshan.fname="Arav"
print(sudarshan.email)

sudarshan.email="This.that@gmail.com"

print(sudarshan.fname)

print(sudarshan.email)

del sudarshan.email

print(sudarshan.email)


