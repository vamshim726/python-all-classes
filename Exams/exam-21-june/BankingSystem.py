'''
3) Build a simple Banking System that allows users to create bank accounts and perform basic 
operations. 
 
Features to Implement: 
1) Create a BankAccount class 
2) Each account should have: 
a. Instance variables: account_number, holder_name, balance 
b. Class variable: bank_name (same for all accounts) 
3) Support the following Instance Methods: 
a. deposit(amount) 
b. withdraw(amount) 
c. check_balance() 
 
4) Include a Class Method: 
a. change_bank_name(new_name) 
 
5) Demonstrate usage by: 
a. Creating 2 or more bank accounts 
b. Performing deposits and withdrawals 
c. Printing details and bank name 

'''



class BankAccount:

    bank_name="Abc Bank"

    def __init__(self, account_number, holder_name, balance ):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{self.holder_name} deposited Rs:{amount}.")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"{self.holder_name} withdrew Rs{amount}.")
         
    def check_balance(self):
         print(f"{self.holder_name}'s Account Balance: ₹{self.balance}")
    
    def print_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ₹{self.balance}")
        print(f"Bank Name: {BankAccount.bank_name}")

    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name



# a. Creating 2 or more bank accounts
account1 = BankAccount("A001", "Alice", 1000)
account2 = BankAccount("A002", "Bob", 500)

# b. Performing deposits and withdrawals
account1.deposit(1500)
account1.withdraw(300)

account2.deposit(1000)
account2.withdraw(2000)  # Should print insufficient balance

# c. Printing details and bank name
account1.print_details()
account2.print_details()

# Changing bank name using class method
BankAccount.change_bank_name("XYZ National Bank")

# Showing updated bank name
print("Updated Bank Name:", BankAccount.bank_name)
account1.print_details()
account2.print_details()



        



