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
  Project Title  : User Management
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
Exercise number 18: 

Description: User Management

Create a simple user management system.

We have a list of users, where each user is represented by a dictionary
containing their information.

users = [
{
"username": "ali",
"age": 25,
"city": "Tehran",
"active": True},
{
"username": "sara",
"age": 17,
"city": "Tabriz",
"active": True}]

You can expand this list using AI.

a) Adding a user

Create a function named:

add_user(users, username, age, city)

This function should:

Create a new user as a dictionary.
Add the new user to the list of users.
Set the `active` value for the new user to `True` by default.
Return the updated list of users.
b) Finding a user

Create a function named:

find_user(users, username)

This function should:

Search through the list of users.
Find the specific user based on the `username`.
Return `None` if the user does not exist.
Return the user's dictionary if the user exists.
c) Checking user access

Create a function named:

check_access(users, username)

This function should check whether the specified user has acces
permission.

Access conditions:

The user's age must be 18 or older.
The user's `active` value must be `True`.

If both conditions are met:

Return `True`.

Otherwise:

Return `False`.

d) Retrieving adult users

Create a function named:

get_adult_users(users)

This function should:

Find only those users who are 18 years of age or older.
Place them into a new list. Finally, return the list.
Final Note

All four functions must be written in the following file:

18_user_management.py

That is, the functions:

add_user()
find_user()
check_access()
get_adult_users()

must all be located within that same file.
    
'''

#%%
'''
Part A of Exercise 18)
'''
 
  
def add_user(users, username, age, city):

    user = {
        "username": username,
        "age": age,
        "city": city,
        "active": True}

    users.append(user)

    return users


users = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True},
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True}]

print(add_user(users, "reza", 30, "Shiraz"))    
    
    
    
#%%
'''
Part B of Exercise 18)
'''

    
def find_user(users, username):

    for user in users:

        if user["username"] == username:
            return user

    return None


print(find_user(users, "ali"))    
    
    
    
    
#%%
'''
Part C of Exercise 18)
'''  
    
    
    
def check_access(users, username):

    for user in users:

        if user["username"] == username:

            if user["age"] >= 18 and user["active"]:
                return True

            return False

    return False


print(check_access(users, "ali"))    
    
    
    
    
    
#%%
'''
Part D of Exercise 18)
'''  
    
def get_adult_users(users):

    adults = []

    for user in users:

        if user["age"] >= 18:
            adults.append(user)

    return adults


print(get_adult_users(users))    
    
    
    
    
    
    
    
        #THE END .... Yours Sincerely .... HFAzar.


