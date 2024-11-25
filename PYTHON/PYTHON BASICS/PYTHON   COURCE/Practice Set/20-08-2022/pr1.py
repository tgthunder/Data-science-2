class Teacher():
    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setadd(self,add):
        self.add=add

    def getadd(self):
        return self.add

    def setsalary(self,salary):
        self.salary=salary

    def getsalary(self):
        return self.salary

class Student(Teacher):
    def setdiv(self,div):
        self.div=div

    def getdiv(self):
        return self.div

    

sudarshan=Teacher()

sourabh=Student()

sourabh.setname('Sourabh')

print(sourabh.getname())

sudarshan.setsalary(24000)

print(sudarshan.getsalary())


