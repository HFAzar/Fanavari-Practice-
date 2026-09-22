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
  Project Title  : Banking System
  Class Session  : 06
  Level          : {level}
  Date           : 1405-06-13
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%

'''
Exercise number 20: 

Description:  Banking System

This is one of the most challenging exercises.

Assume we have bank account information stored in a variable named 
`accounts`:

accounts = [{
"username": "ali",
"password": "1234",
"balance": 5000,
"transactions": []},
{
"username": "sara",
"password": "5678",
"balance": 8000,
"transactions": []}]

a) Account Login

Write a function named:

login(accounts, username, password)

The function must:

Search the `accounts` list for an account with the specified `username`.

Return `None` if such a user does not exist.
If the user exists, check the `username` and `password`.
Return `True` if the username and password match.
Otherwise, return `False`.

b1) Withdrawing Funds – Withdraw

Write a function to withdraw funds.

The function should accept the account and the withdrawal amount as inputs.

For example, the account input could be:

accounts[0]

and the withdrawal amount:

2000

The function must subtract the specified amount from the account's 
`balance` and return the updated account dictionary.

b2) Withdrawing Funds with Transaction Logging

Write the same function as in part b1, but with the following 
differences:

Subtract the amount from the `balance`.
Add the withdrawn amount to the `transactions` list as well.
Finally, return the updated account dictionary.

c1) Depositing Funds – Deposit

Write a function to deposit funds.

The function should operate similarly to part b, but this time add the 
specified amount to the account's `balance`.

c2) Depositing Funds with Transaction Logging

Write the function from part c such that it:

Adds the amount to the `balance`.
Adds the deposited amount to the `transactions` list as well. Return 
the updated account dictionary.
d) Displaying transactions

Write a function named:

show_transactions(account)

This function should accept an account and display or return all 
transactions associated with that account.

e) Fund transfer – Advanced section

Write a function named:

transfer(accounts, sender_username, receiver_username, amount)

For example:

transfer(accounts, "ali", "sara", 1000)

The function must:

Find the sender's account.
Find the receiver's account.
Deduct the amount (1000) from Ali's balance.
Add the same amount to Sara's balance.
Record the transfer transaction in Ali's transaction list.
Record the transfer transaction in Sara's transaction list as well.
Finally, return the updated `accounts` list.
f) Get balance based on currency

Write a function named:

get_balance(account, currency)

This function should accept two inputs:

Account
Currency

The currency should default to USD.

This means if only the account is provided, the balance should be
returned in dollars.

If the currency is RIAL, multiply the dollar balance by the 
dollar-to-rial exchange rate.

For example, if the balance is:

2500 USD

and the exchange rate specified in the exercise is:

2,500,000

then the Rial value is calculated by multiplying the dollar amount by
the exchange rate.

Final file

All functions for this exercise must be written in the following file:

20_bank_system.py

This means, ultimately, we should have the following functions:

login()
withdraw()
deposit()
show_transactions()
transfer()
get_balance()

Exercise 20 consists of 6 main functions.
'''

#%%
'''
Part A of Exercise 20)
'''


def login(accounts, username, password):

    for account in accounts:

        if account["username"] == username:

            if account["password"] == password:
                return True

            return False

    return None


accounts = [
    {
        "username": "ali",
        "password": "1234",
        "balance": 5000,
        "transactions": []},
    {
        "username": "sara",
        "password": "5678",
        "balance": 8000,
        "transactions": []}]

print(login(accounts, "ali", "1234"))




#%%
'''
Part B1 of Exercise 20)
'''

def withdraw(account, amount):

    account["balance"] -= amount

    return account


print(withdraw(accounts[0], 2000))





#%%
'''
Part B2 of Exercise 20)
'''


def withdraw(account, amount):

    account["balance"] -= amount

    account["transactions"].append(-amount)

    return account


print(withdraw(accounts[0], 2000))




#%%
'''
Part C1 of Exercise 20)
'''


def deposit(account, amount):

    account["balance"] += amount

    return account


print(deposit(accounts[0], 1000))




#%%
'''
Part C2 of Exercise 20)
'''

def deposit(account, amount):

    account["balance"] += amount

    account["transactions"].append(amount)

    return account


print(deposit(accounts[0], 1000))




#%%
'''
Part D of Exercise 20)
'''


def show_transactions(account):

    return account["transactions"]


print(show_transactions(accounts[0]))





#%%
'''
Part E of Exercise 20)
'''



def transfer(accounts, sender_username, receiver_username, amount):

    sender = None
    receiver = None

    for account in accounts:

        if account["username"] == sender_username:
            sender = account

        if account["username"] == receiver_username:
            receiver = account

    if sender is not None and receiver is not None:

        sender["balance"] -= amount

        receiver["balance"] += amount

        sender["transactions"].append(-amount)

        receiver["transactions"].append(amount)

    return accounts


print(transfer(accounts, "ali", "sara", 1000))




#%%
'''
Part F of Exercise 20)
'''



def get_balance(account, currency="USD"):

    if currency == "USD":
        return account["balance"]

    if currency == "RIAL":
        return account["balance"] * 2500000








            #THE END .... Yours Sincerely .... HFAzar.
