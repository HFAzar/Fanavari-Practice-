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
  Project Title  : Check Product Inventory
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
Exercise number 15:

Description: Check Product Inventory

Write a function that takes two inputs:
    
1.A dictionary containing product names and their respective stock levels.

2.The name of the specific product.

For example:
    
products = {
"iphone": 5,
"macbook": 2,
"airpods": 0
}

And the product name:
"iphone"

The function should check the stock level of the specified product.
• If the stock level is greater than zero, return `True`.
• If the stock level is zero, return `False`.
For example, for the product "iphone", the output should be `True`.

'''

#%%


def check_product_inventory(products, product_name):
    
    return products[product_name] > 0


products = { "laptop": 3,
              "mouse": 0,
           "keyboard": 5 }

print(check_product_inventory(products, "mouse"))




        #THE END .... Yours Sincerely .... HFAzar.

