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
  Project Title  : calculate grade
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
Exercise number 04:

Description: calculate grade
    

Write a function that takes a score between 0 and 100 and returns the
corresponding letter grade based on the score:

90 to 100 → A 
80 to 89 → B 
70 to 79 → C
60 to 69 → D
Less than 60 → F  
    
'''    
    
#%%   
    
    
def  calculate_grade (scoor):
    
    if   scoor > 100 :
        return "Invalid"
    
    elif scoor < 0 :
         return "Invalid"
    
    elif scoor >= 90 :
        return "A"
    
    elif scoor >= 80 :
        return "B"
    
    elif scoor >= 70 :
        return "C"
    
    elif scoor >= 60 :
        return "D"
    
    else :
         return "F"
     
    
    
     
    #THE END .... Yours Sincerely .... HFAzar.
      
     
        