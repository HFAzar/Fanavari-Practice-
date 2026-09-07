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
  Project Title  : Login System Limited 
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
Exercise number 06:

Description: Login System with Attempt Limit

Exercise No. 5 (Login System) Write a program that displays the 
following message if the user enters the wrong username or password 
more than 3 times:
"User account locked."
After that, do not allow the user to enter a username or password again
and the program ends.   
    
'''
#%%

print ("---------------------------------")
print ("--Welcome to the System Limited--")    
print ("---------------------------------")   
      
 
correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3
logged_in = False

while attempts < max_attempts:
    user_name = input("please enter your username:")
    user_password = input("please enter your password:")

    if user_name == correct_username and user_password == correct_password:
        print("You have logged in successfully")
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("The username or password is incorrect")

if not logged_in:
    print("User account locked")
    
    
    
 #THE END .... Yours Sincerely .... HFAzar.
   
  