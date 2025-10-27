# Define an updated BankAccount class from activity1/task3
# that simulates a bank account with the following new methods:
# (1) deposit_funds - adding money to current balance
# (2) withdraw_funds - withdraw money from current balance. Should check if there is sufficient balance.
# If there is insufficient fund, should not be able to withdraw money. How would you define this method? 
# Should this method return something?
# (3) add_interest - add certain percentage of interest to the current balance

class BankAccount:
    def __init__(self,name,no,balance=10):
        self.holder_name = name
        self.account_no = no
        self.current_balance = balance

    def deposit_funds(self, amount):
        if amount < 0:
            print("Cannot deposit negative amount")
            return
        self.current_balance += amount

    def withdraw_funds(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds")
            return False
        self.current_balance -= amount
        return True

    def add_interest(self, rate):
        if rate < 0:
            print("Interest rate cannot be negative")
            return
        self.current_balance += self.current_balance * (rate / 100)

# Once completed, create an instance of BankAccount with your details and 
# make at least one call to each of the new methods, as well as a call
# to retrieve the current_balance at the end.
account = BankAccount("Your Name", "123456789", 100)
account.deposit_funds(50)
account.withdraw_funds(20)
account.add_interest(5)
print(f"Current balance: {account.current_balance}")
