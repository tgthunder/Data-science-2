inventory = {}
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_val(self):
        print(f"total value of {self.name} = {self.price*self.quantity}")

    def add_product(self):
        global inventory
        inventory[self.name] = self

    def update_stocks(self):
        print("What to Update Price or Quantity?")
        print("Press p for Price and q for quantity: ",end="")
        user_input = input()
        if user_input == "p":
            pr = int(input("Enter Price: "))
            self.price = pr
        elif user_input == "q":
            qu = int(input("Enter Quantity: "))
            self.quantity = qu
        print("Successfully Updated!")


    def print_details(self):
        print("---------------------------")
        print(f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}")
        print("---------------------------")


sofa = Product("Sofa-set",40000,20)
sofa.print_details()
sofa.add_product()
print(inventory['Sofa-set'].name)
dining_table = Product("Dining Table",30000,10)
dining_table.add_product()
dining_table.print_details()
dining_table.calculate_total_val()
office_chair = Product("Office Chair",2300,40)
office_chair.add_product()
print(inventory)
print("--------------------")

dining_table.update_stocks()
dining_table.print_details()




