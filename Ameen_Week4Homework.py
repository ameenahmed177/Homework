# Python Homework (Flow Control, Modules, Functions, Exceptions, NumPy)
# 1. What does one need to do to use a module?
# To use a module, you need to import it using the import keyword followed by the module name.

# 2. Name a Module (not the DateTime Nodule) we looked at and write a line or 2 of code as an example using this module.
# The math module provides mathematical functions and constants. For example, to calculate the square root of a number, you can use the sqrt() function from the math module.

import math

number = 16
square_root = math.sqrt(number)
print(square_root)

# 3. What is a benefit of using Exception handling?
# Exception handling allows you to gracefully handle errors and prevent your program from crashing. It helps you to write more robust code by catching and handling exceptions that may occur during the execution of your program.

# 4. what are the 4 components used for Python Exception Handling?
# The four components used for Python Exception Handling are:
# - try: block of code where you want to catch exceptions
# - except: block of code that handles exceptions
# - else: block of code that executes if no exceptions are raised
# - finally: block of code that always executes, regardless of whether an exception is raised or not

# 5. NumPy arrays are like what Python data type?
# NumPy arrays are like Python lists.

# 6. What is one of the main benefits of using NumPy arrays.
# One of the main benefits of using NumPy arrays is that they are faster and more efficient than Python lists, especially when working with large datasets.

# 7. What is one of the main requirements about the 'dtype' of NumPy arrays?
# One of the main requirements about the 'dtype' of NumPy arrays is that all elements in the array must be of the same data type.

# 8. Of the 10 uses of NumPy, name 2.
# Two uses of NumPy are:
# - Mathematical and logical operations on arrays
# - Handling multi-dimensional arrays for data manipulation.

# 9. Name one of the other libraries we'll use with NumPy?
# One of the other libraries we'll use with NumPy is Pandas.

# 10. What is the shape of NumPy arrays?
# The shape of a NumPy array is the number of elements in each dimension of the array.

# 11. What is a Tensor?
# A tensor is a multi-dimensional array that can represent data in higher dimensions, such as 3D or 4D arrays.

# 12. Name a reason why it's better using NumPy for Data Analysis than using a Python List?
# NumPy is better for data analysis than using a Python list because it provides faster and more efficient operations on large datasets, especially when working with multi-dimensional arrays.
# 13. When creating an "empty" array, where do the elements come from?
# When creating an "empty" array, the elements are not initialized with any specific values. The values in the array are random and depend on the state of the memory.


# Flow Control Methods:
# 1. Create an if statement: if 'age' is greater than or equal to 25, print "Renting a car is more affordable", however if 'age' is less than 25, print "Renting a car is very expensive."

age = 25

if age >= 25:
    print("Renting a car is more affordable")
    
else:
    print("Renting a car is very expensive")

    # 2. Create and chain an if-else statement: if 'age' is greater than or equal to 25, print "Renting a car is more affordable." If 'age' is less than 25 but greater than or equal to 18, print "Renting a car is very expensive." Finally, if age is less than 18, print "You cannot legally rent a car."

age = 18

if age >= 25:
    print("Renting a car is more affordable")

elif age < 25 and age >= 18:
    print("Renting a car is very expensive")

else:
    print("You cannot legally rent a car")

# 3. Loop over the following string to (1) count all the characters in the string and (2) print out all the vowels -- "The quick brown fox jumps over the lazy dog"

string = "The quick brown fox jumps over the lazy dog"
count = 0
vowels = "aeiou"

for char in string:
    count += 1
    if char.lower() in vowels:
        print(char)

# 4. Write a nested loop that prints out every piece of clothing from the couture list, in every fashionable color from the panettone set: couture = ["trousers", "blouse", "bandana", "cumber band", "blazer", "vest", "french beret", "scarf", "stole"] and panettone = {"cerise", "fuchsia", "aqua", "maple", "auburn", "burnt sienna", "gunmetal blue", "Dark Sapphire"}

couture = ["trousers", "blouse", "bandana", "cumber band", "blazer", "vest", "french beret", "scarf", "stole"]
panettone = {"cerise", "fuchsia", "aqua", "maple", "auburn", "burnt sienna", "gunmetal blue", "Dark Sapphire"}

for clothing in couture:
    for color in panettone:
        print(clothing, color)

# 5. Use range as a loop to calculate the sum of all the numbers from 1 to 100

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 6. Print the second item in this fruits list. ["apple", "banana", "cherry"]

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# 7. Change the value from "apple" to "kiwi", in the fruits list. ["apple", "banana", "cherry"]

fruits[0] = "kiwi"
print(fruits)

# 8. Use the append method to add "orange" to the fruits list. ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)

# 9. Use the insert method to add "lemon" as the second item in the fruits list. ["apple", "banana", "cherry"]

fruits.insert(1, "lemon")
print(fruits)

# 10. Use the remove method to remove "banana" from the fruits list. ["apple", "banana", "cherry"]

fruits.remove("banana")
print(fruits)

# 11. Use negative indexing to print the 3rd and 2nd to last items in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[-3], fruits[-2])

# 12. Use a range of indexes to print the third, fourth, and fifth item in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[2:5])

# 13. Use the correct syntax to print the number of items in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(len(fruits))

# 14. Use the correct syntax to sort this list in reverse order ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

fruits.reverse()
print(fruits)

# 15. Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.

import datetime as dt

current_date = dt.datetime.now()
month = current_date.strftime("%B")
print(month)


# 16. Write a simple function that takes 2 parameters -- a first name and a day name.

# Set a default value for the day name of Sunday.
# Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.
# Invoke this function with 2 variables.
# Invoke this function with 1 variable only.

def greeting(first_name, day_name="Sunday"):
    print(f"Hi {first_name}! Happy {day_name}!")

greeting("Ameen", "Friday")
greeting("Ameen")

# 17. Write a block of code to handle one of the most common Python exception errors. Select one of the common errors from the curriculum section on Python Exception handling. Have your code example uses the try,except, else, and finally components.

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Try block executed successfully")
finally:
    print("This block will always execute")
