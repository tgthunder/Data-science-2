class Duck:
    def talk(self):
        print("Qack! Quak!")

class Human:
    pass
    # def talk(self):
        # print("Hi! Hello")

def call_talk(obj):
    obj.talk()

x=Duck()
y=Human()

call_talk(x)

print('--------------')

call_talk(y)

