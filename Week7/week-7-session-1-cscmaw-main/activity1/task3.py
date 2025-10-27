# Define a BankAccount class with the following fields:
# (1) holder_name
# (2) account_no
# (3) current_balance

# The value to each field needs to be provided when an instance of BankAccount is created.
# Write code to create an instance of BankAccount

class BankAccount:
    def __init__(self,name,no,balance=10):
        self.holder_name = name
        self.account_no = no
        self.current_balance = balance



# Write code to create an instance of BankAccount
account1 = BankAccount("John Doe", "123456789", 1000)

# Write code to print the details of the bank account
print(f"Holder Name: {account1.holder_name}")
print(f"Account No: {account1.account_no}")
print(f"Current Balance: {account1.current_balance}")

# Once done, create another instance of BankAccount with only holder's name and 
# account number, and then print the all details of the new instance.
account2 = BankAccount("Jane Smith", "987654321")
print(f"Holder Name: {account2.holder_name}")
print(f"Account No: {account2.account_no}")
print(f"Current Balance: {account2.current_balance}")
