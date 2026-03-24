class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Fonds insuffisants")
        return self

    def display_balance(self):
        print(f"{self.account_holder} : {self.balance}")
        return self
