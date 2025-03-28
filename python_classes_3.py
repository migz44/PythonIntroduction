# Account

class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Congrutulations Your Deposit Was Succesfull. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, You don't have enough money")
        else:
            self.balance -= amount

    def details(self):
        print(f'Account number: {self.acc_number}')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
        print("--------------------------------")

account_1 = Account("001", "Hamilton", 20000)
account_2 = Account("002", "Verstappen", 20000)

account_1.deposit(1000)
account_1.withdraw(200)
account_1.details()