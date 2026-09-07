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
  Project Title  : Simple chatbot 
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
Exercise number 08:

Description: Simple chatbot

Write a simple chatbot that initially displays the following message:
"hello"
Then, every time the user enters something, the chatbot will very simply
display the following response:
    
[chatbot reply]

This process continues until the user types "bye".
In this case, the chatbot should display the following message:
    
"Goodbye"

And the conversation ends.
    
'''

#%%   
    
print ("---------------------------------")
print ("----Welcome to the Chatbot----")    
print ("---------------------------------")     
    

print ("hello")    

while True:
    user_input = input("plaese enter your coment:") 
    if user_input == "bye":
        break
    
    print ("chatbot reply")
    
    
print ("Good Bye" )    
    
    
   #THE END .... Yours Sincerely .... HFAzar.
   
     