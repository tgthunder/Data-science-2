class Student:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.lp=self.Laptop()

    def display(self):
        print('Name is:',self.name)
        print('Roll No is:',self.roll_no)
    
    class Laptop:
        def __init__(self):
            self.brand='Hp'
            self.proccessor='I5'
            self.ram=8
        def Show(self):
            print(f"The brand is {self.brand} and the proccessor is {self.proccessor} and the ram is {self.ram}")


s1=Student('Navin',2)

print(s1.display())

print('---------------------------------')

print(s1.lp.Show())


