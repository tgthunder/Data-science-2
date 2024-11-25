#Create a class Employee with attributes name, salary, and role. Implement a method to give a raise to the employee.

class Employee:
    def __init__(self,name,sal,role):
        self.name = name
        self.sal = sal
        self.role = role

    def increament(self,perc):
        self.sal = self.sal + ((self.sal*perc)/100)
        return self.sal
    
s = Employee('Sudarshan',1500,'Data Analyst')
print(s.increament(30))

