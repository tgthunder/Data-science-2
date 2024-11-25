# constructors in super class are available to sub class

class Father:
    def __init__(self):
        self.property=50000.00

class Son(Father):
    
    def __init__(self):


        
        self.paisa=30000.00

s=Son()

print(s.paisa)

