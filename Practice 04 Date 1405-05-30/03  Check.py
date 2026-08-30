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
  Project Title  : check 
  Description    : check mouse
  Class Session  : 04
  Level          : {level}
  Date           : 1405-05-30
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Exercise number 03:

Description:

We have a list of products, as described, get the product name from the user.
If it is in the list, display "Product is available in the list" and if it
is not in the list, display "Product is not available in the list".

'''
#%%
  

print("----Welcome to the computer store----")

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

product_name = input(" please inter product name:" ).strip().lower()

if product_name.lower() in [product.lower() for product in products]:               
    
    print ("Product is available in the list" )

else:
    print("Product is not available in the list" )





#THE END .... Yours Sincerely .... HFAzar.


