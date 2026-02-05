class BankAccount:
    def __init__(self, name, balance):
        if not name or balance < 0:
            raise ValueError("Invalid name or balance")
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount

    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")


# -------- Main Execution --------
try:
    acc = BankAccount("Jeevan", 1000)  # create account
    acc.deposit(500)  # valid deposit
    acc.withdraw(2000)  # overdraft attempt
except ValueError:
    print("Security Alert: Overdraft attempt detected!")

acc.display_balance()
