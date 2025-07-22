

class BankAccount:
    def __init__(self,acc_num,balance):
        self.acc_num=acc_num
        self.balance=balance


    #overloading + operator
    def __add__(self,other):
        print('adding two account balances')
        return self.balance + other.balance
    
    #overloading * operator
    def __mul__(self,other):

        print('multiplying two account balances')
        return self.balance*other.balance

    def __gt__(self,other):

        return self.balance > other.balance

ba1=BankAccount('123456',2021)
ba2=BankAccount('567891',500)


print(ba1+ba2)
print(ba1*ba2)
print(ba1>ba2)
        