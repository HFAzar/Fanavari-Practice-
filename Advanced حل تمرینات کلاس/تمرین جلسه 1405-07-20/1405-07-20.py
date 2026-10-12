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
  Project Title  : Part 1  &  2
  Class Session  : 06 Advanced
  Level          : {level}
  Date           : 1405-07-20
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {The exercise has not been pushed to GitHub.
================================================
'''
#%%
'''
Exercise number 01 Part 1:

Description: Write a program that takes a number from the user and prints
double that value. Handle non-numeric input using `try/except` and display an
appropriate message instead of letting the program crash. 
''' 


try:
    user_number = int(input("please enter your number:"))
    result = user_number * 2
    print(result)
except ValueError: 
    print("Please enter the number correctly.")


#%%
'''
Exercise number 02 Part 1:

Description: Write a program that takes two numbers from the user and divides 
the first number by the second. Handle the `ZeroDivisionError` and print an 
appropriate message in the event of division by zero.
'''


try:
   user_number1 = int(input("please enter your number1:"))
   user_number2 = int(input("please enter your number2:"))
   result = user_number1 / user_number2
   print(result)
except ZeroDivisionError:
   print("You cannot divide by zero.")
   

#%%
'''
Exercise number 03 Part 1:

Description: Write a function named `safe_int(value)` that converts the input 
value to an `int`. If the conversion is not possible, return `None` 
(handle both `ValueError` and `TypeError`).
'''


def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

#%%
'''
Exercise number 04 Part 1:

Description: Write a program using a loop that repeatedly asks the user for a
number and continues to prompt them until a valid number is entered. Once a 
valid number is received, print it and terminate the loop.
'''



while True:
    try:
        user_number = int(input("please enter your number:"))
        print(user_number)
        break
    except ValueError:
        print("Please enter a valid number.")
        

#%%
'''
Exercise number 05 Part 1:

Description: Assume `data = [1, 2, 3]`. Get an index from the user and print 
the corresponding element. Handle `IndexError` (index out of range) and 
`ValueError` (non-numeric input) with two separate messages.
'''



data = [1, 2, 3]
try:
    index = int(input("please enter your number:"))
    print(data[index])
except ValueError:
   print("Please enter a valid number.")
except IndexError:
    print("Index out of range.")

#%%
'''               
⚜️ Conclusion of the 1 section's exercises and commencement of the 2 section's 
exercises.
'''

#%%
'''
Exercise number 01 Part 2:

Description: Write a program that writes your name and age to a file named
"info.txt", with each on a separate line.
'''


with open("info.txt", "w") as file:
    file.write("HFAzar\n")
    file.write("33\n")


#%%
'''
Exercise number 02 Part 2:

Description: Open the info.txt file and print its contents to the screen.
'''


with open("info.txt", "r") as file:
   print(file.read())



#%%
'''
Exercise number 03 Part 2:

Description: Add a new line to the end of an existing file without erasing the
previous content.
'''


with open("info.txt", "a") as file:
    file.write("This is a new line for Exercise number 02 Part 2.\n")




#%%
'''
Exercise number 04 Part 2:

Description: Write a program that reads a text file and prints the number of 
lines, words, and characters it contains.
'''



with open("info.txt", "r") as file:
    text = file.read()
    print(len(text.splitlines()))
    print(len(text.split()))
    print(len(text))


#%%
'''
Exercise number 05 Part 2:

Description: Write a program that copies the contents of a text file to
another file and converts the characters to uppercase during the process.
'''



with open("info.txt", "r") as source:
    text = source.read()

with open("info_upper.txt", "w") as destination:
    destination.write(text.upper())


#%%
'''
Exercise number 06 Part 2:

Description: Read a file containing a list of numbers (one number per line)
and print their sum.
Use `try/except` to ignore lines that do not contain valid numbers 
(for example, empty lines or lines containing text).
'''


with open("numbers.txt", "w") as file:
    file.write("7\n13\n17\n33\n72\n")

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        try:
            total += int(line)
        except ValueError:
            continue
print(total)


#%%
'''
Exercise number 07 Part 2:

Description: Check whether a file exists using `os.path.exists()`. If it does
not exist, create it and print an appropriate message; if it does exist, 
display its contents.
'''


import os

if os.path.exists("info.txt"):
    with open("info.txt", "r") as file:
        print(file.read())
else:
    with open("info.txt", "w") as file:
        file.write("This file was created.\n")
    print("File did not exist, so it was created.")
    
    

#%%
'''
Exercise number 08 Part 2:

Description: Always use the "with" statement for working with files. Explain 
what problems might arise if we open a file and forget to close it (close()),
and how "with" solves this problem.
'''

'''
Answer:
If we open a file and forget to close it using close(), several problems may 
occur:
1. Resource leak: The file remains open and consumes system resources such as 
memory and file handles.
2. Data loss: Any data written to the file may not be saved properly to disk.
3. File locking: The file may remain locked, preventing other programs from 
accessing or modifying it.
4. Program instability: In large programs, having too many open files can cause
the program to slow down or even crash.

The "with" statement solves this problem by automatically closing the file 
after the block of code is finished.
Even if an exception or error occurs inside the "with" block, the file is still
closed properly.
This ensures that resources are released, data is saved correctly, and the code
is cleaner and safer,
without needing to manually call close().
'''























