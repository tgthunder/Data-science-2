

class Sample:
    y=12
    def __init__(self):
        self.x=10

    @classmethod
    def modify_1(cls,new_y):
        cls.y=new_y

    def modify(self):
        self.x+=1
        

s1=Sample()
s2=Sample()

print('x in S1',s1.x)
print('x in S2',s2.x)

print('y in s1',s1.y)
print('y in s2',s2.y)

print('-------------------------')

print('For modify method')

s1.modify()

print('x in s1',s1.x)
print('x in s2',s2.x)

s1.modify_1(15)

print(s1.y)

print(s2.y)

