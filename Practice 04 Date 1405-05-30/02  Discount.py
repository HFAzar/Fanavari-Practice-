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
  Project Title  : Discount
  Description    : Discount Practice
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
Exercise number 02:

Description:

Get the price of the product from the user.
If the price is more than one million Tomans, a 20% discount is applied 
to the price. If it is between 500,000 Tomans and one million, a 15% 
discountis applied. If the price of the product is less than 500,000 Tomans,
a 10% discount is applied and the final price is displayed.

'''
#%%

print("----Welcome to the online shop----")
  
Product_Price = input("please inter your price:" ).strip()

if Product_Price.isdigit():
    Product_Price= int(Product_Price)

    if Product_Price >= 1000000 :
        new_price1= int (Product_Price * 0.8) 
        print(new_price1 ,"Thanks" )
    
    elif Product_Price >= 500000 :
        new_price2= int( Product_Price * 0.85 )
        print(new_price2 ,"Thanks" )

    else :
        new_price3= int( Product_Price * 0.9 )
        print(new_price3 ,"Thanks" ) 

else:
    print("Enter the correct number")






#THE END .... Yours Sincerely .... HFAzar.
