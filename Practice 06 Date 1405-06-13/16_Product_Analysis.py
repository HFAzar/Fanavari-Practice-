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
  Project Title  : Product Analysis
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
Exercise number 16: 

Description: Product Analysis

We have a list of products where each product is represented by a
dictionary. Each dictionary contains the product code, product name,
and product price.

products = [
{'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
{'code': 'z2', 'name': 'zara shooes 100', 'price': 45},
{'code': 'z3', 'name': 'zara cloth 451', 'price': 35},
{'code': 'z4', 'name': 'zara shooes 300', 'price': 55},
{'code': 'z5', 'name': 'zara shooes 231', 'price': 60},
{'code': 'z6', 'name': 'zara bag 400', 'price': 110},
{'code': 'z7', 'name': 'zara bag 500', 'price': 95}
]

a) Product Price

Write a function that takes the list of products and a product code as
input and returns the price of that product.

For example, for code 'z7', the output should be 95.

b) Product Name

Write a function that takes the list of products and a product code as
input and returns the name of the product associated with that code.

For example, for code 'z7', the output should be:

zara bag 500

c) Complete Product Information

Write a function that takes the list of products and a product code as
input and returns a tuple containing the product code, product name, 
and price.

For example, for code 'z7', the output should look like this:

('z7', 'zara bag 500', 95)

'''
#%%
'''
Part A of Exercise 16)
'''


def get_product_price(products, product_code):
    for product in products:
        if product["code"] == product_code:
            return product["price"]


products = [
    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
    {'code': 'z2', 'name': 'zara shooes 100', 'price': 45},
    {'code': 'z3', 'name': 'zara cloth 451', 'price': 35},
    {'code': 'z4', 'name': 'zara shooes 300', 'price': 55},
    {'code': 'z5', 'name': 'zara shooes 231', 'price': 60},
    {'code': 'z6', 'name': 'zara bag 400', 'price': 110},
    {'code': 'z7', 'name': 'zara bag 500', 'price': 95}]

print(get_product_price(products, "z7"))


#%%
'''
Part B of Exercise 16)
'''

def get_product_name(products, product_code):
    for product in products:
        if product["code"] == product_code:
            return product["name"]


products = [
    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
    {'code': 'z2', 'name': 'zara shooes 100', 'price': 45},
    {'code': 'z3', 'name': 'zara cloth 451', 'price': 35},
    {'code': 'z4', 'name': 'zara shooes 300', 'price': 55},
    {'code': 'z5', 'name': 'zara shooes 231', 'price': 60},
    {'code': 'z6', 'name': 'zara bag 400', 'price': 110},
    {'code': 'z7', 'name': 'zara bag 500', 'price': 95}]

print(get_product_name(products, "z7"))


#%%
'''
Part C of Exercise 16)
'''

def get_product_info(products, product_code):
    for product in products:
        if product["code"] == product_code:
            return (
                product["code"],
                product["name"],
                product["price"] )


products = [
    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
    {'code': 'z2', 'name': 'zara shooes 100', 'price': 45},
    {'code': 'z3', 'name': 'zara cloth 451', 'price': 35},
    {'code': 'z4', 'name': 'zara shooes 300', 'price': 55},
    {'code': 'z5', 'name': 'zara shooes 231', 'price': 60},
    {'code': 'z6', 'name': 'zara bag 400', 'price': 110},
    {'code': 'z7', 'name': 'zara bag 500', 'price': 95}]

print(get_product_info(products, "z7"))




        #THE END .... Yours Sincerely .... HFAzar.

