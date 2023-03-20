# Import the necessary modules
import math
import os
from datetime import datetime

# Define a function that takes two parameters and returns their sum
def add_numbers(x, y):
    return x + y

# Define a class that represents a bank account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

# Create an instance of the BankAccount class
my_account = BankAccount("John Doe", 1000)

# Use the deposit() and withdraw() methods
print("Initial balance:", my_account.balance)
print("Deposit:", my_account.deposit(500))
print("Withdraw:", my_account.withdraw(200))

# Use the add_numbers() function
result = add_numbers(3, 4)
print("Sum:", result)

# Use the math module to calculate the square root of a number
result = math.sqrt(16)
print("Square root:", result)

# Use the os module to get the current working directory
result = os.getcwd()
print("Current working directory:", result)

# Use the datetime module to get the current date and time
now = datetime.now()
print("Current date and time:", now)

# Use a for loop to iterate over a range of numbers
for i in range(5):
    print(i)

# Use a while loop to repeatedly execute a block of code
i = 0
while i < 5:
    print(i)
    i += 1

# Use a list to store multiple values
my_list = [1, 2, 3, 4, 5]

# Use a for loop to iterate over the items in a list
for item in my_list:
    print(item)

# Use the len() function to get the number of items in a list
print("Number of items in my_list:", len(my_list))

# Use the input() function to get input from the user
name = input("What is your name? ")
print("Hello,", name)

# Use the print() function to display output
print("This program demonstrates various basic and intermediate concepts of Python.")