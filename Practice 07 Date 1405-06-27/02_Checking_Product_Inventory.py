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
  Project Title  : Checking Product Inventory 
  Class Session  : 07
  Level          : {level}
  Date           : 1405-06-27
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Exercise number 02:

Description: Checking Product Inventory
You have a dictionary containing products and their stock levels. Take this 
dictionary as input for a function and return two outputs—specifically, two lists:
    
•	One list containing the names of products that are in stock.
•	One list containing the names of products that are out of stock.

inventory = { “apple”: 20, “banana”: 5, “orange”: 0, “milk”: 12,
             “bread”: 0 }
''' 
#%%



inventory = { "apple": 20, "banana": 5, "orange": 0, "milk": 12,"bread": 0 }

def products_in_stock (inventory):
    stock_products = []
    out_of_stock_products = []    

    for product, quantity in inventory.items():
        if quantity > 0 :
            stock_products.append(product)

        else:
            out_of_stock_products.append(product)

    return stock_products , out_of_stock_products











