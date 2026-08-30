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
  Project Title  : short
  Description    : short Name
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
Exercise number 08:

Description:

We have a list of usernames and we want to count the number of names
that are less than 5 in length.

'''  

users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']

new_users = []
count = 0

for i in users:
     new_users.append(len(i))
     if len(i) < 5:
      count = count +1 
      
print(count)

               





#THE END .... Yours Sincerely .... HFAzar.


