class A:
    def meth(self):
        return f"This is a Class A method"

class B(A):
      def meth(self):
        return f"This is a Class B method"

class C(A):
      def meth(self):
        return f"This is a Class C method"

class D(C,B):
    def meth(self):
        return f"This is a Class D method"
    

a=A()
b=B()
c=C()
d=D()

print(d.meth())