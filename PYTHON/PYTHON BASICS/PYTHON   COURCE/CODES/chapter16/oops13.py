class A:
    classvar1="This is class variable of class A"
    def __init__(self):
        self.var2="I am inside class A's constructor"
        self.classvar1="I am instance variable in class A"
        self.special="Special"

class B(A):
    classvar1="I am class variable in class B"    #(overriding)
# I have overrided all the things from class A to access them we use super 
    def __init__(self):
        super().__init__()
        self.var2="I am inside class A's constructor"
        self.classvar1="I am instance variable in class A"

    

a=A()
b=B()

print(b.special)
# first it will check instance variable then only class varables