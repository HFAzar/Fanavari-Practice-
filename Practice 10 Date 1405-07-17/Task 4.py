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
  Project Title  : Store Inventory Management System
  Class Session  : 10
  Level          : {level}
  Date           : 1405-07-17
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Task number 04: 

Description: Store Inventory Management System

OOP · Class · init · self · Methods · str
Design a class named "Product" to manage the details of products in a store.
Each product must have the following attributes:
name
price
quantity
category

Required methods:
1.	__init__() — Initializes the product attributes.
2.	__str__() — Provides a readable and organized display of the product details.
3.	update_price() — Changes the product's price.
4.	add_stock() — Increases the inventory quantity.
5.	sell() — Sells a specified number of units and decreases the inventory.
6.	apply_discount() — Applies a percentage-based discount.
7.	total_value() — Calculates the total value of the inventory for a product.

Example usage:
p1 = Product("Laptop", 50000000, 5, "Electronics")
print(p1)
p1.sell(2)
p1.apply_discount(10)
p1.add_stock(3)
print(p1.total_value())

Rules: The price cannot be negative. The inventory quantity cannot fall below 
zero. The discount must be between 0% and 100%. If there is insufficient stock, 
the sale operation should not be performed.
Extra Challenge: Create several objects of the "Product" class, store them in 
a list, and identify the product with the highest total inventory value.
'''
#%%

class Product:
    def __init__(self, name, price, quantity, category):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return (f"[{self.category}] {self.name} - "
                f"Price: {self.price:,.0f} - "
                f"Qty: {self.quantity} - "
                f"Stock Value: {self.total_value():,.0f}")

    def update_price(self, new_price):
        if new_price < 0:
            print("Error: invalid price")
            return
        self.price = new_price

    def add_stock(self, amount):
        if amount <= 0:
            print("Error: amount must be positive")
            return
        self.quantity += amount

    def sell(self, amount):
        if amount <= 0:
            print("Error: amount must be positive")
            return False
        if amount > self.quantity:
            print(f"Not enough stock (only {self.quantity} left)")
            return False
        self.quantity -= amount
        return True

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Error: discount must be between 0 and 100")
            return
        self.price = self.price * (100 - percent) / 100

    def total_value(self):
        return self.price * self.quantity


def show_inventory(items):
    print("=" * 55)
    for item in items:
        print(item)
    print("=" * 55)


def find_best_product(items):
    best = items[0]
    for item in items:
        if item.total_value() > best.total_value():
            best = item
    return best


if __name__ == "__main__":
    inventory = [
        Product("Laptop", 50_000_000, 5, "Electronics"),
        Product("Phone", 20_000_000, 10, "Electronics"),
        Product("Notebook", 80_000, 200, "Stationery"),
    ]

    show_inventory(inventory)

    laptop = inventory[0]
    print("-- Selling 2 laptops --")
    if laptop.sell(2):
        print("Sale completed")
    laptop.apply_discount(10)
    laptop.add_stock(3)
    print(laptop)

    print("-- Selling more than stock (error test) --")
    laptop.sell(100)

    print("-- Invalid discount (error test) --")
    laptop.apply_discount(150)

    best = find_best_product(inventory)
    print(f"\nBest product by stock value: {best.name}")



    print("\n-- Testing negative price in __init__ --")
    try:
        bad = Product("Bad", -500, 10, "Test")
    except ValueError as e:
        print("Caught error:", e)


























