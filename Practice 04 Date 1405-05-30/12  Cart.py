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
  Project Title  : Cart 
  Description    : Shopping Cart
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
Exercise number 12:

Description:

Using a for loop, write a system that receives the name of a product
from the user 5 times ( Zara,Nike,Adidas,Wilson,Puma,Sport,Jordan )
and if the length of the product name is less than 6, puts it into a
list called shopping cart.
  
'''
#%%

print("-----Welcome to the Sport Shoping-----")

my_list = [ "Zara","Nike","Adidas","Wilson","Puma","Sport","Jordan" ]              

shopping_cart = []

for i in range(5):
    product_name = input("Please enter the product name:".strip())
    if len(product_name) < 6:
        shopping_cart.append(product_name)

print("Shopping cart:", shopping_cart)





#THE END .... Yours Sincerely .... HFAzar.

