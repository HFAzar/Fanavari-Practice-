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
  Project Title  : Login System  
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
Exercise number 05:

Description: Login System
  
Design a login system that asks the user for a username and password.

Valid username:
admin
Valid password:
1234

Until the user enters the correct username and password, the program
will prompt him/her to log in again and display the following message:
"The username or password is incorrect."
If the information is entered correctly, the following message will be
displayed:
"You have logged in successfully." 
    
'''   
    
#%%    
    
       
print ("---------------------------------")
print ("----- Welcome to the System -----")    
print ("---------------------------------")   
    
    
while True:
    user_name=input(" plaese enter your name:")
    user_password=int(input("please enter your password:"))
    
    if not user_name=="admin" or not user_password==1234:
        print ("The username or password is incorrect")
        continue
    else:
        print("You have logged in successfully")
        break 
    
    
    
    
    
    
    
 #THE END .... Yours Sincerely .... HFAzar.
   
    
    