class Bankaccount:
    def __init__(self,account_num,name):
        self.account_num = account_num
        self.name = name
        self.bal = 0

    def deposit(self,amt):
        self.bal = self.bal + amt
        print("Amount deposited successfully!")

    def withdraw(self,amt):
        if amt < self.bal:
            self.bal = self.bal - amt
        else:
            print("Not enough balance to withdraw!")
        
        print(f"Available balance: {self.bal}")

sudarshan = Bankaccount('72152921G','Sudarshan')

sudarshan.deposit(1600)
sudarshan.withdraw(200)
print(sudarshan.account_num)
        
    

        