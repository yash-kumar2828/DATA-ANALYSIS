class Bank():

    def __init__(self,x):
        self.__balance = x


    def get_balance(self,password):
        if password == '1234':
            return self.__balance


    def deposite(self,amount):
        if amount>0:
            self.__balance = self.__balance+amount


b = Bank(490300)
print(b.get_balance('1234'))

b.deposite(10000)
print(b.get_balance('1234'))