class Student:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m

    def talk(self):
        print(f"Hi my name is {self.name}")

        print(f"Hi I got {self.marks} marks")


s1=Student()

print(s1.talk())

print('------------------------------')

s2=Student('Rohit Rana',390)

print(s2.talk())
