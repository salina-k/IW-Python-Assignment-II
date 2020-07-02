# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to my Banking Application")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = BankAccount()
s.deposit()
s.withdraw()
s.display()