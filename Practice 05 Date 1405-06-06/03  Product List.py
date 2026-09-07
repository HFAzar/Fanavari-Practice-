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
  Project Title  : Product List  
  Class Session  : 05
  Level          : {level}
  Date           : 1405-06-06
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%

'''
Exercise number 03:

Description: Product List

Continuously ask the user for product names and put each product into
a list called "products".
This should continue until the customer enters "exit".
After entering "exit", display the entire list of products.

'''

#%%


products=[]

print("---welcome To the online shop---")  
           
print("Enter 'exit' to finish and display the products")  

user_products =input("Please Enter Products  Name:")

while user_products != "exit":
        
    products.append(user_products)
    
    user_products = input("Please Enter Products Name:")
    
print(products)





#THE END .... Yours Sincerely .... HFAzar.

