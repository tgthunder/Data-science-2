


class Dad:
    basketball=1
    

class Son(Dad):
    dance=2
    def isdance(self):
        return f'Yes I can Dance {self.dance} no of styles'
    

class Grandson(Son):
    
    dance=4
    def isdance(self):
        return f'HI Mykle jakson! \nYes I can Dance {self.dance} no of styles'
    

larry=Dad()
garry=Son()
harry=Grandson()


print(harry.isdance())