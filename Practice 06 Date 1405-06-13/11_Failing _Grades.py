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
  Project Title  : Failing Grades
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
Exercise number 11:

Description: Failing Grades

a) Write a function that takes a list of grades, removes the failing 
grades, and returns the list of passing grades.

Example:
Input:   [18, 7, 13, 9, 20, 5]
Output:  [18, 13, 20]

b) Now, take the same input and, this time, return the list of failing
grades.
Output:  [7, 9, 5]

c) Now, take the same input and, instead of returning a list, return the
number of people who passed.

Output:
    
'''
#%%

'''
Part A of Exercise 11)
'''

Scores = [18 , 12 ,10 , 20 , 7 ,16 , 5 , 11 , 13 , 17 , 8 , 2 ,15 ]    


def Failing_Grades ( Scores ) :
    
    Passes = []
    for score in Scores:
        if score >= 10 :
            Passes.append(score)
            
    return Passes


Passes = Failing_Grades(Scores)   
    
print(Passes)    
    



#%%

'''
Part B of Exercise 11)
'''   
 

   
Scores = [18 , 12 ,10 , 20 , 7 ,16 , 5 , 11 , 13 , 17 , 8 , 2 ,15 ]    


def Failing_Grades ( Scores ) :
     
     Failed = []
     for score in Scores:
         if score < 10 :
             Failed.append(score)
             
     return Failed


Failed = Failing_Grades(Scores)   
     
print(Failed)    
        
    
    
    
 #%%

'''
Part C of Exercise 11)
'''   
     
    
Scores = [18 , 12 ,10 , 20 , 7 ,16 , 5 , 11 , 13 , 17 , 8 , 2 ,15 ]    


def Failing_Grades ( Scores ) :
    
    count = 0
    for score in Scores:
        if score >= 10 :
            count += 1
                       
    return count

count = Failing_Grades(Scores)   
    
print(count)    
    
    
    
    
    
    
        #THE END .... Yours Sincerely .... HFAzar.

    
    
    
    
    
    
