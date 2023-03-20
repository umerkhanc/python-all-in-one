# Import the necessary modules
import math
import random

# Define a function that takes two parameters and returns their sum
def add_numbers(x, y):
    return x + y

# Define a class that represents a rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of the Rectangle class
my_rectangle = Rectangle(5, 10)

# Use the area() and perimeter() methods
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())

# Use the add_numbers() function
result = add_numbers(3, 4)
print("Sum:", result)

# Use the math module to calculate the square root of a number
result = math.sqrt(16)
print("Square root:", result)

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

# Use the random module to generate a random number
result = random.randint(1, 6)
print("Random number:", result)
