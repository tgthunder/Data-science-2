# # multilevel inheritance
# class Dad:
#     Football=1

# class Son(Dad):
#     Dance=2
#     Football=3
#     def isdance(self):
#         return f"Yes I can dance {self.Dance} no of styles"

# class Grandson(Son):
#     Dance=10
#     def isdance(self):
#         return f" mickel jakson \nYes I can dance {self.Dance} no of styles"

# Harry=Dad()
# Larry=Son()
# Garry=Grandson()

# print(Garry.isdance())
# print(Larry.Football)
# print(Garry.Dance)
# print(Garry.Football)

# Exercise
class Electronic_Gagetes:
    Hardware="ic's","Diode","Registers","wires","pins","batteries"
    def hardware(self):
        return f"there are {self.Hardware} hardware present"
    print(type(Hardware))
    

class Pocket_devices(Electronic_Gagetes):
    def fun(self):
        return f"{self} are pocket devices"

    

class Phone(Pocket_devices):
    apps=["calculator","whatsapp","Gmail"]
    games=["pubg","free fire","angry bird"]
    def Apps(self):
        return f"there are {self.apps} apps"
    def game(self):
    
        return f"There are {self.games} games"

Computer=Electronic_Gagetes()
calculator=Pocket_devices()
Samsung=Phone()
print(Samsung.fun())

# print(Samsung.game())
# print(Computer.hardware())
