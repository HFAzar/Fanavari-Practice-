'''
     * In The Name Of God *
''' 
#              H
#             /|\
#            / | \
#           /--F--\
#          / \ | / \
#         *--- A ---*
#          \ / Z \ /
#           \  A  /
#            *-R-*
#             \ /
#          ====*=====
#          | HFAZAR |
#          ==========
'''
================================================
  Author         : HFAzar
  Project Title  : Bank Account and Money Transfer Simulator
  Class Session  : 10
  Level          : {level}
  Date           : 1405-07-17
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Task number 05: 

Description: Bank Account and Money Transfer Simulator

OOP · Object Interaction · Methods · Lists · Error Handling
Design a simple banking system that allows users to create accounts, increase 
their balance, make withdrawals, and transfer money between different accounts.
The main class should be named `BankAccount`.
Attributes for each account:
`owner`
`account_number`
`balance`
`transactions`

Required methods:
1.	`__init__()` — Initialize an account with its initial details.
2.	`__str__()` — Display account information.
3.	`deposit()` — Deposit an amount into the account.
4.	`withdraw()` — Withdraw funds (with a balance check).
5.	`transfer()` — Transfer money to another instance of the `BankAccount` class.
6.	`get_balance()` — Display the current balance.
7.	`transaction_history()` — Display the history of deposits, withdrawals, 
and transfers.

Example usage:
ali = BankAccount("Ali", "1001", 5000000)
sara = BankAccount("Sara", "1002", 2000000)
ali.deposit(1000000)
ali.withdraw(500000)
ali.transfer(sara, 2000000)
print(ali)
print(sara)

ali.transaction_history()

Rules: 
    Deposit, withdrawal, and transfer amounts must be positive. Withdrawing 
more than the available balance is not permitted. A failed transfer must not 
alter the balance of any account. Account numbers must be unique.
Bonus Challenge: Create another class named `Bank` that maintains a list of 
all accounts and provides functionality to create accounts, search for an 
account, and display the total balance across the bank.
'''
#%%


class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return (f"Account {self.account_number} | "
                f"Owner: {self.owner} | "
                f"Balance: {self.balance:,.0f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Error: deposit amount must be positive")
            return
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount:,.0f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: withdrawal amount must be positive")
            return False
        if amount > self.balance:
            print("Insufficient balance")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdraw: -{amount:,.0f}")
        return True

    def transfer(self, other, amount):
        if amount <= 0:
            print("Error: transfer amount must be positive")
            return False
        if amount > self.balance:
            print("Transfer failed: insufficient balance")
            return False
        self.balance -= amount
        other.balance += amount
        self.transactions.append(f"Transfer to {other.owner}: -{amount:,.0f}")
        other.transactions.append(f"Transfer from {self.owner}: +{amount:,.0f}")
        return True

    def get_balance(self):
        return self.balance

    def transaction_history(self):
        print(f"Transaction history for account {self.account_number}:")
        if not self.transactions:
            print("  (no transactions yet)")
            return
        for t in self.transactions:
            print(f"  - {t}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, owner, account_number, balance=0):
        for acc in self.accounts:
            if acc.account_number == account_number:
                print("Error: account number already exists")
                return None
        new_acc = BankAccount(owner, account_number, balance)
        self.accounts.append(new_acc)
        return new_acc

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)


if __name__ == "__main__":
    bank = Bank("Bank Melli")

    ali = bank.create_account("Ali", "1001", 5_000_000)
    sara = bank.create_account("Sara", "1002", 2_000_000)

    ali.deposit(1_000_000)
    ali.withdraw(500_000)
    ali.transfer(sara, 2_000_000)

    print(ali)
    print(sara)
    print()

    ali.transaction_history()
    print()
    sara.transaction_history()

    print(f"\nTotal bank balance: {bank.total_balance():,.0f}")

    print("\n-- Error tests --")
    ali.withdraw(100_000_000)              # insufficient balance
    ali.transfer(sara, -50_000)            # negative amount
    bank.create_account("Reza", "1001", 0) # duplicate account number

    print("\n-- Testing negative initial balance --")
    try:
        bad_acc = BankAccount("Bad", "9999", -1000)
    except ValueError as e:
        print("Caught error:", e)
        
        
        
        
        
        
        
        
        
        
