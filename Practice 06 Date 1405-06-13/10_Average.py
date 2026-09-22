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
  Project Title  : Average
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
Exercise number 10:

Description: Average

Write a function that takes a list of scores, calculates their average,
and returns it.

Constraint:
You are not allowed to use built-in Python functions, such as "sum()".
    
'''

#%%


Scores = [18 , 12 ,10 , 20 , 7 ,16 , 5 , 11 , 13 , 17 ]    
    
def  Average ( Score ):
    
    total = 0
    for i in Score :
      total += i
    Average = total / len(Score)    
    
    return Average
    
result = Average ( Scores )    
    
print (result)    
    
    
    
    
    
    
        #THE END .... Yours Sincerely .... HFAzar.
 
    
    
    