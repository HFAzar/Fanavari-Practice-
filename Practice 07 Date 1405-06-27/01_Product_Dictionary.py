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
  Project Title  : Product Dictionary 
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
Exercise number 01:

Description: Working with a Product Dictionary

We have a dictionary of products:
products = { ‘laptop’: 1200, ‘phone’: 800, ‘tablet’: 500, 
            ‘headphone’: 150, ‘mouse’: 50 }

Write several functions that take this dictionary as input and:
•	Return the highest price.
•	Return the name of the product with the highest price.
•	Perform the same two tasks for the lowest price.
•	Return the total sum of the product prices.
•	Return the average of the product prices.
    
''' 
#%%

products = {"laptop" : 1200, "phone": 800, "tablet": 500, 
            "headphone": 150, "mouse": 50 }

def product_max_price (products):
    return max(products.values())
        



def product_max_price_name (products): 
    max_name =""
    max_value = 0
    for product,value in products.items():
        if value >  max_value :
          max_value =  value
          max_name = product
                   
    return max_name
 



def product_min_price_name (products): 
    min_name =""
    min_value = list(products.values())[0]
    for product,value in products.items():
        if value <  min_value :
          min_name = product
          min_value = value        
    return min_name
 



def total_product_price (products): 
    return sum(products.values())




def total_product_average_price (products): 
    return (sum(products.values())/ len(products.values()))









