class Car:
    def __init__(self,company ,color,model,engine_type):
        self.company = company
        self.color = color
        self.model = model
        self.engine_type = engine_type

    
    def print_details(self):
        print(f"Comapny name: {self.company}\nColor: {self.color}\nModel: {self.model}\nEngine_type: {self.engine_type}")

c1 = Car("Toyota","White","Fortuner","bs6")
c2 = Car("BMW","Red","X7","bs7")

print("------------------")
c1.print_details()
print("------------------------")
c2.print_details()
print("-------------")