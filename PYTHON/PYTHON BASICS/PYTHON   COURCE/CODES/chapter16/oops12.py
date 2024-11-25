# diamond shaped problems(more on overriding)
class A:
    def meth(self):
        print("This is a method of class A")
class B(A):
     def meth(self):
        print("This is a method of class B")
class C(A):
    def meth(self):
        print("This is a method of class C")
    
class D(C,B):
    def meth(self):
        print("This is a method of class D")
    
a=A()
b=B()
c=C()
d=D()

b.meth()


