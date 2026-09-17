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
  Project Title  : Check password
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
Exercise number 07:

Description: Check password

a)
Write a function that receives the "password" and has the following conditions:
Have at least 8 characters.
have at least one number.
There should be at least one letter in it.
If the password meets the above conditions, just print this statement:
"password sabt shod"
If it does not meet the conditions, print:
"password kamel nist"


b)
Write the same function as before, but if the password is correct,
do not print anything;instead, return "True".Otherwise, return "False".


c)
Create a function named "check_password_strength" that evaluates
password strength and returns a number between 1 and 4:

4: If the password has more than 8 characters and includes letters 
(both uppercase and lowercase) and numbers.

3: If the password has more than 8 characters and includes letters and
numbers.

2: If the password has more than 8 characters.

1: If the password has fewer than 8 characters.   
 
'''
#%%
'''
Part A of Exercise 07)
    
''' 


def Check_password(Password):

    my_number = False
    my_letter = False

    if len(Password) >= 8:

        for i in Password:

            if i.isdigit():
                my_number = True

            elif i.isalpha():
                my_letter = True

        if my_number and my_letter:
            print("password sabt shod")
        else:
            print("password kamel nist")

    else:
        print("password kamel nist")


Password = Check_password("Hfa33377")

print(Password)


#%%
'''
Part B of Exercise 07)
    
''' 

def Check_password(Password):

    my_number = False
    my_letter = False

    if len(Password) >= 8:

        for i in Password:

            if i.isdigit():
                my_number = True

            elif i.isalpha():
                my_letter = True

        if my_number and my_letter:
            return True
        else:
            return False

    else:
        return False


Password = Check_password("Hfa33377")

print(Password)



#%%
'''
Part C of Exercise 07)
    
''' 

def check_password_strength(Password):
    
    if len(Password) < 8:
        return 1

    my_letter = False
    my_number = False
    my_upper  = False
    my_lower  = False

    for i in Password:
        
        if i.isalpha():
            
            my_letter = True
            
        if i.isdigit():
            
            my_number = True
            
        if i.isupper():
            
            my_upper = True
            
        if i.islower():
            
            my_lower = True

    if my_letter and my_number and my_upper and my_lower:
        
        return 4
    
    elif my_letter and my_number:
        
        return 3
    
    else:
        
        return 2


    
Password = check_password_strength("Hfa123456")

print (Password)





        #THE END .... Yours Sincerely .... HFAzar.
    
    