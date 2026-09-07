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
  Project Title  : students names  
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
Exercise number 02:

Description: Displaying the names of accepted students

We have a list of student names and their scores. At the end, display 
only the names of the students who were accepted.
Optional: Also rank the accepted students based on their scores.

students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20, 17, 9, 13, 7, 20, 18, 3, 1, 14]

'''

#%%


   #     حالت اول که نمرات از کم به زیاد مرتب شده است    #




students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20, 17, 9, 13, 7, 20, 18, 3, 1, 14]
count = 0
result = sorted(zip(scores, students))

for score, student in result:
    if score >= 10:
        count = count + 1
        print(count, "-", student, score)





#%%


   #     حالت دوم  نمرات از زیاد به کم مرتب شده است    #



students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20, 17, 9, 13, 7, 20, 18, 3, 1, 14]
count = 0
result = sorted(zip(scores, students), reverse=True)

for score, student in result:
    if score >= 10:
        count = count + 1
        print(count, "-", student, score)








#THE END .... Yours Sincerely .... HFAzar.

