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
  Project Title  : sale 
  Description    : Selling products
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
Exercise number 11:

Description:

We have a list of product purchase prices and a list of product sales
prices. We need to calculate the profit for each product in a list
separately.


buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]

'''   
#%%
            
                       #  روش اول  کد نویسی به روش لیست  #                        

buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]

Profit = []

for i in range(len(buy_prices)):
    p = sell_prices[i] - buy_prices[i]
    Profit.append(p)

print("Profit:", Profit)



#%%
                       #  روش دوم  کد نویسی به روش دیکشنری  #                        


Shopping_list = {"a":14000,
                 "b":16800,
                 "c":24500,
                 "d":35400,
                 "e":44000,
                 "f":110000,
                 "g":233000}
 
Sell_list = {"a":17500,
             "b":20100, 
             "c":23500,
             "d":41000,
             "e":53000,
             "f":104000,
             "g":325000}

Profit_of_each_product = []

Total_profit = 0

for i in Shopping_list : 

    Profit = Sell_list[i] - Shopping_list[i]
    Profit_of_each_product.append(Profit)
    Total_profit = Total_profit + Profit

print("Profit of each product:", Profit_of_each_product)
print("Total profit:", Total_profit)





#THE END .... Yours Sincerely .... HFAzar.

