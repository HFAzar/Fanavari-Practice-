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
  Project Title  : check email
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
Exercise number 06:

Description: check email
    
Write a function that receives an email and checks if the email is valid
or not.
How to find out if the email is valid?
There should be no "space" between email characters.
It must contain the "@" sign.
It must have the word ".com".
If the email was valid, the function should return "True"; Otherwise it
should return "False".   
    
'''
#%%
    
    
def  check_email ( Email ):
    
    if " " in Email:
        return False
        
    elif not "@" in Email: 
        return False
        
    elif not ".com" in Email :
        return False 
     
    else:
        return True
    
Email = check_email("Hfazar@_77@gmail.com")    
    
print(Email)    
    
    
    
    
    
    
    #THE END .... Yours Sincerely .... HFAzar.
 
    
   