# class Father:
#     def __init__(self,property):
#         self.property=property

#     def fathdetails(self):
#         return f"The fathers property is {self.property} "

# class Son(Father):
#     def __init__(self, propertyson=0,property=0):
#         super().__init__(property)
#         self.propertyson=propertyson

#     def Sondetails(self):
#         print( "The Total property of son is  ",self.propertyson+self.property)
    
# s=Son(200,500)

# s.Sondetails()



class Square():
    def __init__(self,x):
        self.x=x

    def area(self):
        print('The area of square is ',self.x*self.x)

class Rectangle(Square):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        super().area()
        print('The area of rectangle is ',self.x*self.y)

a,b=[float(x) for x in input("Enter the numbers:").split(',')]

r=Rectangle(a,b)
r.area()
