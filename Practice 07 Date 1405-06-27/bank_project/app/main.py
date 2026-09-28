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
  Project Title  : main.py
  Class Session  : 07
  Level          : {level}
  Date           : 1405-06-27
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Exercise number 04:

Description: 
    
    bank_project/
│
├── bank/
│   ├── account.py
│   └── fees.py
│
└── app/
├── main.py   <<====*****
└── calculator.py
    
    
''' 
#%%


from bank.account import show_balance
from app.calculator import deposit
from bank.fees import apply_fee


balance = 1000
print(show_balance(balance))

balance = deposit(balance, 500)
print(show_balance(balance))

balance = apply_fee(balance, 50)
print(show_balance(balance))










