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
  Project Title  : Online Store
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
Exercise number 19: 

Description: Online Store

We have a small store with product information structured as follows:

products = [
{"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
{"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
{"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
{"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]

a) Finding a product

Write a function named:

find_product(products, code)

This function should accept the product code.

If the product is found, return the dictionary corresponding to that 
product.
If the product is not found, return `None`.

b) Adding a product to the shopping cart

Write a function named:

add_to_cart(products, cart, code)

This function should:

Accept the list of products.
Accept the shopping cart list.
Accept the product code.
If the product exists and `stock > 0`, add the product to the `cart`.
Finally, return the `cart`.

c) Adding to the cart and reducing stock

Write the same function as in part (b), but this time, if the product
exists and its stock is greater than zero:

Add the product to the `cart`.
Decrease the product's stock in the `products` list by one.
Finally, return the `products` list.

d) Advanced section

Perform the same task as in part (c), with the difference that the 
function must:

Add the product to the `cart`.
Decrease the product's stock in `products` by one.
Finally, return both items:
`cart`
`products`

Meaning the function should have two outputs.
'''


#%%
'''
Part A of Exercise 19)
'''

    
def find_product(products, code):

    for product in products:

        if product["code"] == code:
            return product

    return None


products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}]


print(find_product(products, "p2"))    
    
    
    
#%%
'''
Part B of Exercise 19)
'''
    
    
def add_to_cart(products, cart, code):

    for product in products:

        if product["code"] == code and product["stock"] > 0:
            cart.append(product)
            return cart

    return cart


cart = []

print(add_to_cart(products, cart, "p2"))    
    
    
    
    
    
#%%
'''
Part C of Exercise 19)
'''
        
    
def add_to_cart(products, cart, code):

    for product in products:

        if product["code"] == code and product["stock"] > 0:

            cart.append(product)

            product["stock"] -= 1

            return products

    return products


cart = []

print(add_to_cart(products, cart, "p2"))    
    




#%%
'''
Part D of Exercise 19)
'''


def add_to_cart(products, cart, code):

    for product in products:

        if product["code"] == code and product["stock"] > 0:

            cart.append(product)

            product["stock"] -= 1

            return cart, products

    return cart, products


cart = []

result = add_to_cart(products, cart, "p2")

print(result)









            #THE END .... Yours Sincerely .... HFAzar.


