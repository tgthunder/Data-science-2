#36. Develop a class `Student` with attributes: name, age, and a list of subjects. Implement methods to calculate GPA and display details.

class Student:
    def __init__(self,name,age,subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def print_subject(self):
        for i in self.subjects:
            print(i,end = " ")

    
        