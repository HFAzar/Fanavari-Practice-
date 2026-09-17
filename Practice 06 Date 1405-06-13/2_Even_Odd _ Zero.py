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
  Project Title  : Even,Odd & Zero 
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
Exercise number 02:

Description: Even,Odd & Zero
    
Create a file and write the following functions:
    
a) A function that takes a number and returns "Even" if it is even,
and "Odd" if it is odd.

b) A function that takes a number and returns "True" if it is even,
and "False" if it is odd.

c) A function that takes a number and returns "Positive" if it is
positive, "Negative" if it is negative, and "Zero" if it is zero.    
    
'''

#%%
'''
Part A of Exercise 02)
'''   
   

def check_number(Number):
    if Number % 2 == 0 :
      return "Even"  
  
    elif Number % 2 != 0 : 
        return "Odd"
    
Number = check_number(72)   
print (Number)    
    
    
    
#%%
'''
Part B of Exercise 02)
'''   
   


def check_number(Number):
    if Number % 2 == 0 :
      return "True"  
  
    elif Number % 2 != 0 : 
        return "False"
    
Number = check_number(77)   
print (Number)    
    
    


#%%
'''
Part C of Exercise 02)
'''   
   


def check_number(Number):
    if Number > 0 :
      return "Positive"  
  
    elif Number == 0 : 
        return "Zero"
    
    else:
        return "Negative"
    
    
Number = check_number(-0.1)   
print (Number)    
    
    








   #THE END .... Yours Sincerely .... HFAzar.



    
    