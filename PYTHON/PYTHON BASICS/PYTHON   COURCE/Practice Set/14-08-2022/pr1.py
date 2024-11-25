class Student:
    Schoolname='CHC'
    def __init__(self,fname,lname,roll_no,city):
        self.fname=fname
        self.lname=lname
        self.roll_no=roll_no
        self.city=city
    
    @classmethod
    def newname(cls,snewname):
        cls.Schoolname=snewname

    @staticmethod
    def addition():
        return 34+50


sudarshan=Student('Sudarshan','Sutar',58,'Kolhapur')

# print(sudarshan.lname)
# 
# print(sudarshan.addition())

# sudarshan.newname('VHV')

# print(sudarshan.Schoolname)



print(id(sudarshan))

print(id(Student))



