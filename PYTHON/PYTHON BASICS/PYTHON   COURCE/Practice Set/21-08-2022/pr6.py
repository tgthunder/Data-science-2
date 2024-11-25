# Operator Overloading

print(23+45)

s="Sudarshan"
s1=" Sutar"
print(s+s1)

l1=[2,7,-56,12]
l2=[12,67,27]

print(l1+l2)

class Bookx:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages

class Booky:
    def __init__(self,pages):
        self.pages=pages

 



x=Bookx(1200)
y=Booky(1500)
#
print('Total pages are ',x+y)


