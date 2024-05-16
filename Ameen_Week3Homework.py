# 1. What is an algorithm?
# An algorithm is a step-by-step procedure or formula for solving a problem.

# 2. Variable names may not start with certain characters - name two.
# - Numbers (e.g., 1, 2, 3)
# - Special characters (e.g., #, $, @)

# 3. What is a Semantic error?
# A Semantic error is an error in logic or meaning in the code,
# where the program runs without crashing but produces incorrect results.

# 4. What is the #1 rule of coding / debugging?
# The #1 rule of coding / debugging is: Always read and understand error messages.

# 5. List 5 Python reserved words.
# - def
# - for
# - if
# - return
# - import

# 6. Write a multi-line string with your name, favorite food, and dream job on 3 different lines
info = """
Ameen Ahmed
pizza
Statistician
"""

# 7. Assign 5 different data types to 5 different variables. At least one datatype must be a string
# String
favorite_color = "blue"

# Print the length of your string
len(favorite_color)

# Print the index value of the 4th character in your string
favorite_color[3]

# Integer
age = 35

# Float
GPA = 3.89

# List
favorite_final_fantasy_games = ["FINAL FANTASY XIII", "FINAL FANTASY XIII-2", "LIGHTNING RETURNS: FINAL FANTASY XIII", "FINAL FANTASY XV WINDOWS EDITION", "FINAL FANTASY VII REMAKE INTERGRADE"]

# Boolean
isExcellentWithNumbers = True

# 8. Create a new variable called savvy, and assign it the string with this phrase "Learning Data Analytics and Python is Awesome!"
savvy = "Learning Data Analytics and Python is Awesome!"

# Return a range of characters that slices the above string from the beginning of "ing" up to before "and"
print(savvy[5:24])

# Replace "Awesome" with "great" in the string
savvy = savvy.replace("Awesome", "great")

# Test and print the savvy string to see it contains "Python"
print(savvy)

# 9. Create and assign 3 more variables called name, age and length using the multi-variable naming method
name, age, length = "Ameen", 35, 171

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."
miniBio = f"Hi my name is {name}, I am {length} cm tall and {age} years old today."

# Print 'miniBio'
print(miniBio)

# Cast and print the age variable to a float
print(float(age))

# 10, Create a list of at least 5 elements of mixed data types
mixed_list = [17, 3.14, "Python", True, [1, 2, 3]]

# Replace a part of it with something else
mixed_list[1] = 3.89

# Append or insert several more items to the list
mixed_list.append("Tennis")

# Find and print the length of the list
print(len(mixed_list))

# Slice a sub-section of the 1st list, and save it to a different 2nd list
slice_mixed_list = [mixed_list[4]]

# Print the 2nd list
print(slice_mixed_list)

# Extend your original list with the 2nd list sliced above
slice_mixed_list.extend([4, 5, 6])

# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean
simList = ["FINAL FANTASY XIII", "FINAL FANTASY XIII-2", "LIGHTNING RETURNS: FINAL FANTASY XIII", "FINAL FANTASY XV WINDOWS EDITION", "FINAL FANTASY VII REMAKE INTERGRADE"]

# Sort "simList", and print the list
simList.sort()
print(simList)

# Copy the "simList" list to another 3rd list
simList_copy = simList.copy()

# Add the 2nd and 3rd lists together into a 4th list
simList_combine = simList + simList_copy

# 12. Create a set of about 3 elements
my_set = {"apple", "banana", "cherry"}

# Add a list of fruits to the above set and print the result
fruit_list = ["orange", "blueberry", "kiwi"]
my_set.update(fruit_list)
print(my_set)

# Add a car element to your set
my_set.add("Toyota Camry")

# Create a 2nd set with a few odd items
second_set = {"pineapple", 42, 3.14, False, "electric guitar"}

# Save the union of 1st set and 2nd set to a 3rd set
third_set = my_set.union(second_set)

# Pop an element from the 2nd set, and print the remainder of the set
second_set.pop()
print(second_set)

# Clear the 1st set and print the result
my_set.clear()
print(my_set)

# Discard an element, and remove another element from the 3rd set
third_set.discard("apple")
third_set.remove("pineapple")

# Print the remainder of the 3rd set
print(third_set)

# 13. Create a dictionary with at least 5 values of different data types
my_dict = {"FINAL FANTASY XIII" : 2010, "GPA" : 3.89, "favorite_games" : ["FINAL FANTASY XIII", "FINAL FANTASY XIII-2", "LIGHTNING RETURNS: FINAL FANTASY XIII", "FINAL FANTASY XV WINDOWS EDITION", "FINAL FANTASY VII REMAKE INTERGRADE"], "completed" : True}

# Print out 1 value
print(my_dict["FINAL FANTASY XIII"])

# Replace any one value in your dictionary with your name
my_dict["GPA"] = "Ameen"

# Add your favorite color to the dictionary
my_dict["favorite_color"] = "blue"

# Add a list, tuple or set to your dictionary
my_dict["ice_cream_flavers"] = ("chocolate", "vanilla", "strawberry")

# Print a list of the dictionary keys
print(my_dict.keys())

# Print a list of the dictionary values
print(my_dict.values())

# Copy your 1st dictionary into a 2nd dictionary
my_dict_copy = my_dict.copy()

# Pop an item from the 2nd dictionary, and print the dictionary
my_dict_copy.pop("GPA")
print(my_dict_copy)

# Remove all the elements from the 2nd dictionary and print the result
my_dict_copy.clear()
print(my_dict_copy)
