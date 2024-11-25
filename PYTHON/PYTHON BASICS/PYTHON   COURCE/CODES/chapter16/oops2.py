class Employee:
    no_of_leaves=10 # this is called class variables
    


sudarshan=Employee()
sourabh=Employee()


sudarshan.name="Sudarshan"
sudarshan.salary=34500
sudarshan.task="Investor"


sourabh.name="Sourabh"
sourabh.salary=5000
sourabh.task="Manager"


print(sourabh.salary)
print(sudarshan.name)
# no of leaves for all class object is same
print(sudarshan.no_of_leaves)
print(Employee.no_of_leaves)
print(sourabh.no_of_leaves)
print(sourabh.__dict__)
# we can not change the value of template by class objects 
sourabh.no_of_leaves = 12 # this will make a new object variable
print(sourabh.__dict__)
print(Employee.no_of_leaves)
Employee.no_of_leaves=12
print(Employee.no_of_leaves)
print(sudarshan.no_of_leaves)
print(Employee.__dict__)
