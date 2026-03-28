# Program ID: G401
# Exercise Type: Data Types and Type Identification
# Tasks Included:
# - Task 1: Identify and categorize values into correct data types
# - Task 2: Declare variables and check their data types using type()
# - Task 3: Determine appropriate data types for real-world examples

# Original code starts below

# Level 1
# Part 1 Python Syntax
# G401 - Four Musketeers
# In the previous class you learnt how to use:
# - Arithmetic operators with variables.
# - BODMAS in Python programs
# Today you will learn about types of data, variables can store.
# Look at the lists given below.
# Each list has an odd one, who happens to be our hidden "DataType".
# Can you identify the odd one out?
# List 1: 78 , 100, 45, book
# List 2: hello, cat, 24, pencil
# List 3: 45, 7.3, 21, 11
# List 4: True, 34, 21, 11
# Great, you have identified the odd one out. Here they are:
# List 1: book
# List 2: 24
# List 3: 7.3
# List 4: True
# String is a data type containing characters. In the List 1 example, it is: "Book"
# Integer is a data type that means numbers without a decimal point. In the List 2 example, it is 24
# Float is a data type that stands for numbers with decimal pointsIn the List 3 example, it is 7.3
# Boolean is a data type that can have only two values: True or False. In the List 4 example, it is True
"""-----------Task 1: Four Musketeers ---------------"""
print(" ")
print("*** Task 1: ***")
# Given below are a set of  values (separated by commas). 
# , , , , “Hello World!”, , “A”, 
# Place them against the correct data type print statement. Once done uncomment the statements and click Run. 
# The first one has been done for you.
print("String Data Type:  Hello World!, A")
print("Integer Data Type:10 -54")
print("Float Data Type:3.14 -42.43")
print("Boolean Data Type:True False")

"""-----------Task 2: Variable Game ---------------"""
print(" ")
print("*** Task 2: ***")
# Uncomment the statements below and run them
a=93.4
b=-52
c="Welcome to the world of data types"
d=True
print(a)#Float
print(b)#Integer
print(c)#String
print(d)#Boolean
# Did you get any errors? 
# No errors - as the print statement will print any data type value on to the output terminal ( as it treats everything as a string)
# How would you know the data type of the variable? Is there a way to find out? 
# Let's check it out.
# Uncomment the statements below and click Run
print("Check the Data types")
print("Data type of a is: ", type(a))
print("Data type of b is: ", type(b))
print("Data type of c is:", type(c))
print("Data type of d is:", type(d))
#The type() function tells you the data type of the variable 

"""-----------Task 3: Whats the data type? ---------------"""
print(" ")
print("*** Task 3: ***")
# Ready for a quick check. 
# What is the data type you will use  for the following?
# Uncomment the print statements, type the data type after the colon and click Run.
# The first one is done for you
print("Name of your friend: String")
print("Your schools name: string ") 
print("Your age: Integer")
print("Your height in feet:Float?")
print("Do you have a sibling: Book")#False
print("Color of the leaf: String")
print("Number of books in your shelf: Integer")

"""Great! You are making good progress with the data types."""
