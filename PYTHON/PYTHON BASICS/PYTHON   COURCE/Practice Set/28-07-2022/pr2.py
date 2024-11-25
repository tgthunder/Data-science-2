class A:
    classvar1="I am class variable of class A"

    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="I am instance variable of class A"
        self.special="Special"

class B(A):
    
    classvar1="I am class variable of class B"

    def __init__(self):
        

        self.var1="I am inside class B's constructor"
        self.clasvar1="I am instance variable of class B"
        super().__init__()
        print(super().classvar1)


a=A()
b=B()

print(b.classvar1,b.var1,b.special)
