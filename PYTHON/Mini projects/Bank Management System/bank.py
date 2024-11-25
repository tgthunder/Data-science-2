import sys
class Bank(object):
    """Bank Related Transactions"""
    # To initialize name and available balance
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        return self.balance

    def withdrawal(self,amount):
        if amount>self.balance:
            print("You Have Low Balance to withdrawal")

        else:
            self.balance-=amount
        return self.balance
    
name=input("Enter Your Good Name:")

b=Bank(name)

while(True):
    print('d-Deposit,w-Withdrawal,e-Exit')
    choice=input("Enter Your choice:")
    if choice=='e' or choice=='E':
        sys.exit()
    amt=float(input("Enter the amount:"))

    if choice=='d' or choice=='D':
        print('Balance after deposite:',b.deposite(amt)) 

    else:
        print('Balance after withdrawal:',b.withdrawal(amt)) 


      
    