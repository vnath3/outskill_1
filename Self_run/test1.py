class BankAccount:

    #initializer method as constructor
    def __init__(self, account_number,balance=0.0):
        self.account_number = account_number
        self.__balance = balance # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        
    def get_balance(self):
        if self.__balance > 0:
            print(f"Current balance: {self.__balance}")
        else:
            print("Your account balance is zero or negative.")


cust1 = BankAccount("1234567890", 1000.0)
cust1.get_balance()
cust1.deposit(500.0)
