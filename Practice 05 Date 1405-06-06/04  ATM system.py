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
  Project Title  : Simple ATM system  
  Class Session  : 05
  Level          : {level}
  Date           : 1405-06-06
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%

'''
Exercise number 04:

Description: Simple ATM system
               
Design a simple ATM system.
At first, the following menu will be displayed to the user:
Menu:
• Inventory
• Deposit
• Withdrawal
• Exit
• Other operations
As long as the user selects balance, deposit or withdrawal options, a simple message will be displayed for each; For example:
• "Inventory operation selected."
• "The deposit operation was selected."
• "Withdrawal operation selected."
Then the user is asked:
"Another operation or exit?"
If the user selects another operation, the following menu will be displayed again:
Balance, deposit, withdrawal
But if you choose the exit option, the following message will be displayed:
"Thanks, logout successful."

'''

#%%



print ("----------------------------------")
print ("----- welcome to the bank ATM -----")    
print ("----- Your money is safe here-----")
print ("----------------------------------")


while True:
    print("Menu:\n• Inventory\n• Deposit\n• Withdrawal\n• Exit\n• Other operations")

    user_operation = input(" Please choose an operation:")

    if user_operation =="Inventory":
        print("Inventory operation selected")
    
    elif user_operation =="Deposit":
        print("The deposit operation was selected")

    elif user_operation =="Withdrawal":
        print(" Withdrawal operation selected")

    other_operations = input ("Other operations or Exit ?")
    if other_operations == "Other operations":
        continue
    elif other_operations == "Exit":
        print("Thanks, logout successful")
        break










#THE END .... Yours Sincerely .... HFAzar.


