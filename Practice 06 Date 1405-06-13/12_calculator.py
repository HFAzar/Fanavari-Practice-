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
  Project Title  : calculator
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
Exercise number 12:

Description: calculator

Write a function that takes two numbers and an operator as input.

If the operator is addition, perform the addition and return the result.
If it is subtraction, perform the subtraction and return the result.
If it is multiplication,perform the multiplication and return the result.
If it is division, perform the division and return the result.
If the operator is anything other than addition, subtraction,
multiplication, or division, return `None`.

'''
  
#%%


def calculator(Number1 , Number2 , operation):
    
    if operation == "*" :
        result = Number1 * Number2
        return result
    
    
    elif operation == "/"  :
        result = Number1 / Number2
        return result

    elif operation == "+"  :
        result = Number1 + Number2
        return result 

    elif operation == "-"  :
        result = Number1 - Number2
        return result


    else:
        return None



my_calculator = calculator( 55 , 22 , "*" )

print(my_calculator)




        #THE END .... Yours Sincerely .... HFAzar.


