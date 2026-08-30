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
  Project Title  : Login
  Description    : Login Practice
  Class Session  : 04
  Level          : {level}
  Date           : 1405-05-30
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Exercise number 01:

Description:

Receive username and password from the user and if
username "Admin" and password "1234" :
    "Your login was successful".
Otherwise:
    "The username or password is incorrect".

'''
#%%
 # روش اول برای کد نویسی #                  

      

print("----Welcome to the system----")

username = input("Please inter your username :" ).strip().lower()
password = input("Please inter your password :" ).strip()

if username=="admin":
    if password.isdigit():
        if password=="1234":
            print("Your login was successful") 
        else:
            print("The username or password is incorrect")
    else:
        print("The username or password is incorrect")
else:
    print("The username or password is incorrect")
 




#%%



 # روش  دوم برای کد نویسی #                  



print("----Welcome to the system----")

username = input("Please inter your username :" ).strip().lower()
password = input("Please inter your password :" ).strip()

if username=="admin" and password == "1234":
    print("Your login was successful")
else:
    print("The username or password is incorrect")    
               




#THE END .... Yours Sincerely .... HFAzar.
