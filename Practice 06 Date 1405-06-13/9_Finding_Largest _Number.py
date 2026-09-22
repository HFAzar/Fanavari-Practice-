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
  Project Title  : Finding the Largest Number
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
Exercise number 09:

Description: Finding the Largest Number

Write a function that takes a list of numbers, finds the largest number
in the list, and returns it as the output.

This function performs a task similar to the built-in `max()` function;
therefore, you are not allowed to use `max()`.
    
'''   
    
#%%


Number = [2 , 71 ,19 ,  3 , 5 ,23 , 7 , 29 , 11 , 13 , 17 ,73 ,37  ]    
    
    
def Finding_Largest_Number ( Number ):
    
    largest = Number[0]
    
    for i in Number :
      if i > largest :
          largest = i
    return largest 
     
result =  Finding_Largest_Number (Number)    
print (result)
    
    
    
    
    
    
    
    
 
    
 
        #THE END .... Yours Sincerely .... HFAzar.
  
 
    