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
  Project Title  : name cleaner
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
Exercise number 05:

Description: name cleaner
    

Write a function that takes a first name and a last name as input and 
formats and standardizes them.   
    
'''   
    
#%%


def  name_cleaner(first_name , last_name) :
    
    first_name = first_name.strip().replace(" ", "").title()
    
    last_name = last_name.strip().replace(" ", "").title()
    
    return first_name , last_name 
    
    
Name = name_cleaner( " a  L   i  " ,"  piL e h VAr    ")
    
print (Name)    
    
    
    
    
    
    
    #THE END .... Yours Sincerely .... HFAzar.
 
    
    
    
    