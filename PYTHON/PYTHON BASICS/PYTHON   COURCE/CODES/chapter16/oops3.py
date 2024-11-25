class Employee:
    no_of_leaves=10 # this is called class variables
    # self is a convention in oop of python(self means jis object ke uper ap vo function chalana chahate ho)
    def printdetails(self):
        return f"Name is {self.name} and salary is {self.salary} and task is {self.task}"


sudarshan=Employee()
sourabh=Employee()


sudarshan.name="Sudarshan"
sudarshan.salary=34500
sudarshan.task="Investor"


sourabh.name="Sourabh"
sourabh.salary=5000
sourabh.task="Manager"

print(sourabh.printdetails())
print(sudarshan.printdetails())