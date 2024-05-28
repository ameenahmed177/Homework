# Python Homework (NumPy, Pandas)
# 1. What does Pandas stand for?
# Pandas stands for "Python Data Analysis Library"

# 2. What are the 2 collections used in Pandas?
# The two collections used in Pandas are:
# - Series: a one-dimensional array that can hold any data type
# - DataFrame: a two-dimensional array that can hold multiple data types

# 3. Name 4 things Pandas can do for us.
# Pandas can:
# - Read and write data from various file formats, such as CSV, Excel, and SQL databases
# - Handle missing data and clean up messy data
# - Perform data manipulation and transformation operations
# - Analyze and visualize data using built-in plotting functions

# 4. To permanently sort a DataFrame, which keyword should one use with the df.sort() method?
# To permanently sort a DataFrame, you should use the inplace=True keyword argument with the df.sort() method.

# 5. What is a CSV?
# A CSV (Comma-Separated Values) file is a plain text file that stores tabular data in a structured format, with each row representing a record and each column representing a field or attribute.

# 6. When cleaning data what values do we not like in our data?
# When cleaning data, we do not like missing values, duplicate values, or inconsistent values in our data.


# Please Complete this Coding Exercise:
# 7. Import NumPy, use one of the NumPy methods and create an array with a shape of (2, 3, 2). You can use the reshape method -- .reshape()
import numpy as np

array_arange = np.arange(12).reshape(2, 3, 2)
print(array_arange)

# 8. Use NumPy .linspace() to create an array with 6 linearly spaced values between 0 and 20
array_linspace = np.linspace(0, 20, 6)
print(array_linspace)

# 9. Make a Deep Copy of the above array
array_copy = array_linspace.copy()
print(array_copy)

# 10. Concatenate these 3 arrays into a new array named 'newArray'...
array_arange = np.arange(12).reshape(2, 3, 2).ravel()
print(array_arange)
newArray = np.concatenate((array_arange, array_linspace, array_copy))
print(newArray)

# 11. Sort 'newArray' in order into 'sortedArray'
sortedArray = np.sort(newArray)
print(sortedArray)

# 12. Unpack the array tuples from the above 'reshapedArray' into 2 well named variables. Print the 2 variables.
reshapedArray = np.arange(12).reshape(2, 3, 2)
a, b = reshapedArray
print(a)
print(b)

# 13. Combined and sort the following arrays into one called 'comboArray' ...
one = np.array([10, 11, 12, 13, 14, 15, 16, 17])
two = np.array([20, 21, 22, 23, 24, 25, 26, 27])
three = np.array([ 0, 1, 2, 3, 4, 5, 6, 7])
comboArray = np.concatenate((one, two, three))
comboArray = np.sort(comboArray)
print(comboArray)

# 14. Take 'comboArray' and perform the following slicing activities:
# print sec1 - the 2nd element
sec1 = comboArray[1]
print(sec1)

# print sec2 - all elements from the 3rd element to the last
sec2 = comboArray[2:]
print(sec2)

# print sec3 - all elements from the 4th to the 14th elements
sec3 = comboArray[3:14]
print(sec3)

# print sec4 - the last 6 elements
sec4 = comboArray[-6:]
print(sec4)

# print sec5 - all element from #0 up to and including #15, using the negative number method, i.e. taking a section from the end.
sec5 = comboArray[:-10]
print(sec5)

# print sec6 - from #20 every even element to the end
sec6 = comboArray[16::2]
print(sec6)

# print sec7 - from the last element moving forward, every 5th element.
sec7 = comboArray[-1::-5]
print(sec7)

# 15. Using Series, create a DataFrame that looks like this:
import pandas as pd

Dinner = {
    "Ingredients" : ["Flour", "Milk", "Eggs", "Spam"],
    "Quantity" : [4, 1, 2, 1],
    "Unit" : ["cups", "cup", "large", "can"],
}

df = pd.DataFrame(Dinner)

# 16. Take this data and create a DataFrame named studentData
studentData =     {'Name': ['Jai', 'janusha', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
        'address': ['Delhi', 'Doha', 'Chennai', 'Dakhar'],
        'Age': [21, 23, 24, 21],
        'Pets': ['Dog', 'Bunny', 'Chinchilla', 'Parrot'],
        'sport': ['Darts', 'Basketball', 'PaddleBoarding', 'Cricket']
    }
print(studentData)

# 17. Add a new column to the DataFrame with the following deserts: ["ice cream", "Cashew Fudge", "waffels", "Carrot Halwa"]
studentData['Deserts'] = ["ice cream", "Cashew Fudge", "waffels", "Carrot Halwa"]
print(studentData)

# 18. Sort the 'studentData' DataFrame in Ascending order -- Sorting by column 'Name' and then "address"
studentData = pd.DataFrame(studentData)
studentData.sort_values(by=['Name', 'address'], inplace=True)
print(studentData)

# 19. Save this DataFrame here below to disc as a .CSV file with the name cows_and_goats.csv:
df = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
df.to_csv('cows_and_goats.csv',index=False)

# 20.
# (A) Using Pandas, make your own .CSV file with data on vegetables and save it. 
data = {
    'Vegetable': ['Carrot', 'Broccoli', 'Spinach', 'Potato', 'Tomato'],
    'Color': ['Orange', 'Green', 'Green', 'Brown', 'Red'],
    'Weight (g)': [50, 150, 30, 200, 85]
}
df = pd.DataFrame(data)
df.to_csv('vegetables.csv', index=False)

# (B) Using Pandas, make a change to your CSV file, and save a copy with a different name.
df['Price per kg (USD)'] = [2.5, 3.0, 4.0, 1.5, 2.0]
df.to_csv('vegetables_with_prices.csv', index=False)
