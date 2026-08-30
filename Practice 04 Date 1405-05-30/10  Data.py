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
  Project Title  : data 
  Description    : Temperature data
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
Exercise number 10:

Description:

We have data from a factory sensor that records the temperature 
in Celsius. Create a new list and display the previous numbers 
in Fahrenheit. 

Celsius to Fahrenheit conversion formula : 
 
  *( Farenheit = Celsius * 1.8 + 32 )*             

'''

print("--- Celsius to Fahrenheit Converter ---")

data = [ 27.5 , 21.3 , 29 , 33.3 , 19.8 , 38.2  ]


Farenheit = []

for i in data :
    Farenheit.append(i * 1.8 + 32)
print (Farenheit)



#THE END .... Yours Sincerely .... HFAzar.


