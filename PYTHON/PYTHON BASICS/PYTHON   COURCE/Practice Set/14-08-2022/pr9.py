


class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def display(self):
        print("name is :",self.name)
        print("Age is :",self.age)
        print("salary is :",self.salary)

emp=Employee("Sudarshan",20,50000)

print(emp.name)

emp.display()

print('----------------------------')

class Myclass():
    @staticmethod
    def mymethod(a):
        a.salary+=10000
        a.display()

Myclass.mymethod(emp)

