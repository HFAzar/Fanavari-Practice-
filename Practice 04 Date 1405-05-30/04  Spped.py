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
  Project Title  : Spped  
  Description    : Spped check
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
Exercise number 04:

Description:
    
Get the car speed from the user. If it is more than 120 km/h, display 
"Dangerous". If it is between 80 and 120, display "High speed". 
If it is between 0 and 80, display "Normal speed". If it is below 0, 
display "Car is stationary".
    
'''

Car_Speed = int(input("Enter the speed value:").strip())

if Car_Speed >120 :
    print("Dangerous" )
elif Car_Speed > 80 :
    print("High speed" )
elif  Car_Speed > 0 :
    print("Normal speed" )
elif Car_Speed < 0 : 
    print("Car is stationary" )
else:
    print("Enter the correct speed value" )
               




#THE END .... Yours Sincerely .... HFAzar.



