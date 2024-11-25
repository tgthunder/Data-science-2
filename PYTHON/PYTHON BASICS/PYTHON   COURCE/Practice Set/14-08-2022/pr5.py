class Student:
    # This is a constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("HI name is ",self.name)
        print("Marks are ",self.marks)

    def calculate(self):
        if(self.marks>=600):
            print("YOu have got 1st rank!")
        elif(self.marks>=300 and self.marks<=500):
            print("YOu have got 2nd rank!")
        else:
            print("You have got 3rd rank!")

    def getname(self):
        return self.name

    def setname(self,name):
        self.name=name



n=int(input("How many students do you want?:"))

i=0
while(i<n):
    name=input("Enter your name:")
    marks=int(input("Enter your marks:"))
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print('---------------------------')


