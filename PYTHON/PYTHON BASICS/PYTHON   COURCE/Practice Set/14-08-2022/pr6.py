class Student:
    n=0

    def __init__(self):
        Student.n=Student.n+1

    @staticmethod
    def no_of_objects():
        print('No of objects created =',Student.n)

s1=Student()

s2=Student()

s1.no_of_objects()

