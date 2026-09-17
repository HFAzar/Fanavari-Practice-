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
  Project Title  : calculate age 
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
Exercise number 01:

Description: calculate age

Write a function that takes an input (year of birth), calculates the 
person's age, and returns the age as the output.

A) Write a function that accepts only the year of birth as input.
    
B) Write another function that accepts two inputs: the year of birth 
and the calendar type. If the calendar is Gregorian, calculate the 
age based on the Gregorian calendar; if it is Solar (Shamsi),
calculate the age based on the Solar calendar. For example:
(1377, "Solar")
or:
(1999, "Gregorian")

C) Write the same function as in part (b), but if the function receives
only one input, assume the calendar is Gregorian by default.
    
D) Write the function so that it accepts only one input (year of birth)
but can automatically determine whether the entered year is Gregorian 
or Solar.
  
'''

#%%
'''
Part A of Exercise 01)
    
'''    
    
 
def calculate_age (Year_birth):
    this_year = 1405
    return  this_year - Year_birth   
         
age = calculate_age(1372)

print(age ,"years old")



#%%
'''
Part B of Exercise 01)
    
'''   


def Calendar_Detection (year_birth , Calendar_type ):
    
    
    if Calendar_type == "شمسی" :
        this_year = 1405
        Solar_age = this_year - year_birth
        return Solar_age
                  
    elif Calendar_type == "میلادی" :
        this_year = 2026
        Gregorian_age = this_year - year_birth
        return Gregorian_age
    
    else:
        print("Invalid input" )    
    
Solar_age = Calendar_Detection (1372 , "شمسی" )
Gregorian_age = Calendar_Detection (1993 , "میلادی" )

print(Solar_age ,"شمسی")
print(Gregorian_age , "میلادی")



#%%
'''
Part C of Exercise 01)
    
'''  

def Calendar_Detection(year_birth, Calendar_type = None):  
    
    if Calendar_type == None : 
        this_year = 2026
        Gregorian_age = this_year - year_birth
        return Gregorian_age
    
    elif Calendar_type == "شمسی" :
        this_year = 1405
        Solar_age = this_year - year_birth
        return Solar_age
                  
    elif Calendar_type == "میلادی" :
        this_year = 2026
        Gregorian_age = this_year - year_birth
        return Gregorian_age
    
    else:
        print("Invalid input" )    
    
age = Calendar_Detection(1990)   
      
print(age)   
    
    
    
    
    
   
#%%
'''
Part D of Exercise 01)
    
'''  


def Calendar_Detection(year_birth):  
    
    if year_birth >= 1900  :
        Calendar_type = "Gregorian"
        return Calendar_type


    elif year_birth >= 1300 :
        Calendar_type = "Solar"
        return Calendar_type


age = Calendar_Detection(1372)

print (age)









   #THE END .... Yours Sincerely .... HFAzar.


