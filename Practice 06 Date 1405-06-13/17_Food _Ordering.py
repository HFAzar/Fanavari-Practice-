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
  Project Title  : Food Ordering Program
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
Exercise number 17: 

Description: Food Ordering Program

Create a function that takes no arguments; instead, the function should 
initiate a `while` loop and display a food menu.

The program must repeatedly accept orders from the user via `input` 
until the user enters the word "order".

Once the user enters "order", the process of accepting orders should
stop.

Finally, store all the customer's orders in a list and return that list 
as the function's output.

'''
#%%


def menu_app():

    menu = [
        "pizza",
        "burger",
        "pasta",
        "salad"]

    orders = []

    while True:

        print(menu)

        order = input("Enter your order: ")

        if order == "order":
            break

        orders.append(order)

    return orders


print(menu_app())




        #THE END .... Yours Sincerely .... HFAzar.


