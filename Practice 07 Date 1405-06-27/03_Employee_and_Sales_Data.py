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
  Project Title  : Working with Employee and Sales Data
  Class Session  : 07
  Level          : {level}
  Date           : 1405-06-27
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Exercise number 03:

Description: Working with Employee and Sales Data

Part 1: Employee Data:

Write a function that accepts employee data as input:
employees = { “E01”: { “name”: “Ali”, “age”: 28, “salary”: 3000 }, 
“E02”: { “name”: “Sara”, “age”: 32, “salary”: 4500 }, 
“E03”: { “name”: “Reza”, “age”: 25, “salary”: 2800 } }
•	Return the name of the person with the highest salary.
•	Return the name of the person with the lowest salary.
•	Return a list of names of people earning more than 3000.
•	Write a function that takes two inputs—the `employees` dictionary and a
number—and returns a list of names of people whose salary exceeds that number.
•	Return the average of all salaries.


Part 2: Working with Sales:

Write a function that accepts a list of tuples as input:
sales = ( (“Ali”, “Laptop”, 1200), (“Sara”, “Phone”, 800), (“Ali”, 
“Phone”, 800), (“Reza”, “Laptop”, 1200), (“Sara”, “Laptop”, 1200),
(“Ali”, “Mouse”, 50) )
•	Write a function that returns a dictionary where the keys are the individuals'
names and the values ​​are the total purchase amounts for each person.
•	Write a function that returns a dictionary where the keys are product names 
and the values ​​are the sales counts for each product. •	Write a function that 
outputs a number representing the store's total revenue.
'''
#%%


employees = { "E01": { "name": "Ali", "age": 28, "salary": 3000 }, 
             "E02": { "name": "Sara", "age": 32, "salary": 4500 }, 
             "E03": { "name": "Reza", "age": 25, "salary": 2800 } }

'''
Part 1:
'''


def max_salary_name (employees):
    max_salary_name =""
    max_salary = 0
    for employee_id, data in employees.items():
        salary = data["salary"]
        name = data["name"]
        if salary >  max_salary :
          max_salary =  salary
          max_salary_name = name
                   
    return max_salary_name    




def min_salary_name(employees):
    min_salary_name =""
    min_salary = None
    for employee_id, data in employees.items():
        salary = data["salary"]
        name = data["name"]
        if min_salary == None or salary < min_salary :
          min_salary =  salary
          min_salary_name = name
                   
    return min_salary_name    





def max_salary_personnel (employees):
    names = []
    for employee_id, data in employees.items() :
        salary = data["salary"]
        if salary > 3000 :
           name = data ["name"]
           names.append(name)
      
    return names 
           




def personnel_salary (employees , number):
    names = []
    for employee_id, data in employees.items() :
        salary = data["salary"]
        if salary > number :
          name = data ["name"]  
          names.append(name)
  
    return names
    



def total_average_salary (employees):
    total_salary = 0
    for employee_id , data in employees.items() :
        salary = data ["salary"]
        total_salary += salary
        
    return total_salary / len(employees)


average_salary = total_average_salary(employees)
print(average_salary)

    
    
    
    
    
#%% 
'''
Part 2:
'''
   

sales = ( ("Ali", "Laptop", 1200), ("Sara", "Phone", 800),
         ("Ali", "Phone", 800 ),  ("Reza","Laptop", 1200), 
         ("Sara", "Laptop", 1200), ("Ali", "Mouse", 50) )




def total_buy_per_person (sales):
    total_person_buy = {}
    for name ,product , price in sales :
       if name not in  total_person_buy :
           total_person_buy [name] = 0
    
       total_person_buy [name] += price

    return total_person_buy

 





def number_of_sold (sales):
    product_sales = {}
    for name ,product , price in sales :
        if product not in  product_sales :
            product_sales [product] = 0
            
        product_sales [product] += 1        

    return product_sales 






def total_store_revenue (sales):
    total_Sale = 0
    for name ,product, Sale in sales :
        total_Sale += Sale

    return total_Sale 




