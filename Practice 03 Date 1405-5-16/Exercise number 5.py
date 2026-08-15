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
 Author        : HFAzar
 Description   : Python Practice
 Class Session : 03
 Date          : 1405/05/16
 GitHub        : https://github.com/HFAzar
================================================
'''
'''
Exercise number 5:

Description:   
Zara Shopping Bill. 📊 
'''

print("---- Welcome To Zara Online Shop ----")

Product_Name = input("Please enter the 'NAME' of the chose product:").strip()

Product_Price = float(input("Please enter the 'PRICE' of the chose product:").strip())

Discount_Code = input("Please enter the 'DISCOUNT CODE' product:").strip().upper()


if Discount_Code == "Z14":
    Final_price = Product_Price*0.8   # 20% discount 
    print(Final_price)


else :
    print("Wrong discount code")
    print("You have one chance 1️⃣")
    Discount_Code2 = input("Attention⚠️: Enter the 'DISCOUNT CODE' correctly:").strip().upper()


    if Discount_Code2 == "Z14" : 
       Final_price = Product_Price * 0.8   # 20% discount 
       print(Final_price)


    else:
        print("You have been blocked ⛔")
    


#THE END .... Yours Sincerely .... HFAzar.

