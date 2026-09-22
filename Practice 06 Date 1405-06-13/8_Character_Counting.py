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
  Project Title  : Character Counting
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
Exercise number 08:

Description: Character Counting

Write a function that takes two inputs:

A word

A character

Then, check how many times that character appears in the word and return the count as the output.

Write the function in two ways:

a) Using only a `for` loop

b) Without using a `for` loop
    
'''   
    
#%%

'''
Part A of Exercise 08)
    
'''
   
def Character_Counting( word , char ):
    
    count = 0
    for i in word :
        if i == char:
            count+=1
    return count
    
word = Character_Counting (" The quick brown fox jumping over the lazy dog" , "o" )    
print (word)   
    
    
    
#%%

'''
Part B of Exercise 08)
    
'''

  
def Character_Counting( word , char ):
    
     char_count = word.count(char) 
           
     return char_count
    
word = Character_Counting (" The quick brown fox jumping over the lazy dog" , "o" )    
print (word)   
    
    

    








        #THE END .... Yours Sincerely .... HFAzar.



