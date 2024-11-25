class Bank(object):
    cash=10000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

    def addedcash(cls,added):
        cls.cash=cls.cash+added
        print(cls.cash)

a=Bank()

a.available_cash()

a.addedcash(24)




