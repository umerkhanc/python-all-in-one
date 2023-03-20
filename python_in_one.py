# Declare and initialize variables
x = 5
y = 10

# Use arithmetic operators to perform calculations
result = x + y
print("Sum:", result)
result = x - y
print("Difference:", result)
result = x * y
print("Product:", result)
result = x / y
print("Quotient:", result)
result = x % y
print("Remainder:", result)

# Use comparison operators to compare values
result = x > y
print("x > y:", result)
result = x < y
print("x < y:", result)
result = x == y
print("x == y:", result)
result = x != y
print("x != y:", result)

# Use logical operators to combine conditions
result = (x > 0) and (y > 0)
print("x > 0 and y > 0:", result)
result = (x > 0) or (y > 0)
print("x > 0 or y > 0:", result)
result = not(x > 0)
print("not(x > 0):", result)

# Use if-elif-else statements to control the flow of execution
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

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
print("This is a basic Python program.")
