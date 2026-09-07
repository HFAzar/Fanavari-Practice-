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
  Project Title  : Restaurant 
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
Exercise number 07:

Description: Restaurant Ordering System
  
We have a list of foods which is the restaurant menu. The name of this 
list is "foods".
First, all the foods in the menu should be displayed to the user.
Then the user can select the foods one by one and order them.
Every time the user enters the phrase "order", he will not be asked for
the name of the food and all the orders registered using the "for" loop
should be displayed to him as an invoice.  
 
'''

#%%   
    
print ("---------------------------------")
print ("----Welcome to the Restaurant----")    
print ("---------------------------------") 
    
 
foods = ["Pizza", "Burger", "Pasta", "Salad", "Chicken" , "Coffe" ]   
price = [ 5.25 , 7.5 , 10 , 4.3 , 12.8 , 3.7 ] 
final_order = [] 
  
while True:    
    for food in foods:
        print(food)
    user_order = input ("please enter your order:")
    if user_order in foods:
        final_order.append(user_order)
    if user_order=="order":
       break   
   
print("Bill") 
 
total_price=0     
for user_order in final_order:
    total = zip(foods , price)   
    for food, food_price in total:
        if food == user_order:
            print(food, food_price)
            total_price = total_price + food_price
print("Total:", round(total_price, 2))
    
    
    
    
  #THE END .... Yours Sincerely .... HFAzar.
   
     
    
    