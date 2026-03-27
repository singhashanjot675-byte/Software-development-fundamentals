# Account Class
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")


# Customer Class
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        self.account.display_balance()


# Transaction Class
class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")

# Step 2: Test the functionality

# Create an account for customer
acc1 = Account(101, 500)
cust1 = Customer("Ashan", acc1)

# Display customer details
cust1.display_customer_info()

# Performing transactions
t1 = Transaction(acc1, 200, "deposit")
t2 = Transaction(acc1, 100, "withdraw")
t3 = Transaction(acc1, 1000, "withdraw")  # insufficient funds

# Final account balance
acc1.display_balance()