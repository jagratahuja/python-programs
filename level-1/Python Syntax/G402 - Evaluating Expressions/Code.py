# Program ID: G402
# Exercise Type: Expression Evaluation and Type Conversion
# Tasks Included:
# - Task 1: Evaluate expressions with user input and observe type issues
# - Task 2: Calculate total bill for a stationery shop
# - Task 3: Convert speed from km/hr to m/s
# - Task 4: Calculate area and perimeter of a circle

# Original code starts below

# Level 1
# Part 1 Python Syntax
# G402 - Evaluating Expressions
''' Task 1: '''
print(" ")
print("***** Task 1: *****")

a = input("Enter an integer value ")
b = input("Enter a float value")
c = input("Enter another integer value ")
expr = (a / b) * c
print ("result is: ", expr)


''' Task 2: '''
print(" ")
print("***** Task 2: *****")


''' Task 3: '''
print(" ")
print("***** Task 3: *****")


''' Task 4: '''
print(" ")
print("***** Task 4: *****")# What if you have a variable of int data type but now want it to be used with values with decimals?
# Can you convert an integer data type  to float data type? 
# Do you know of functions that can help in conversion?
# Let us take a look
"""-----------Task 1: Expression Galore ---------------"""
print(" ")
print("*** Task 1: ***")
# Uncomment the statements and click Run:
a = int(input("Enter an integer value "))
b = float(input("Enter a float  value"))
c = int(input("Enter another integer value "))
expr =  (a / b) * c
print ("result is: ", expr)
# Did you get an error? Do you know why? 
# When you divide a number the result can be a decimal number.
# You got an error because when you use both integer and float data types, the computer gets confused.
# So you need to convert the variables to float data type. Do you know why we convert it to float data type? 
# The mathematical calculation can give you a result with decimals. So we will have to convert it to float data type. 
# To convert a variable to float data type, we use the float() function
#For example:
#d = input("Enter an integer value ")
#d=float(d)
# Go back to your code above and convert the int variable to float.
# Hint: You can do the following after accpeting the value from the user:
  #a = float(a)
  #b = float(b)
  #c = float(c)



"""-------Task 2: Visit to the Stationery Shop -----------"""
print(" ")
print("*** Task 2: ***")
# Ready to write a program using different data types.
# Let's start by visiting the stationery shop.
# Ryan has been asked to take care of the accounts at the new stationery shop. 
# The shop sells the following items:
# A Pack of Pencils (20 in number) - Rs.75
# A Pack of BallPoint Pens(5 in number)- Rs.30
# Long Size Notebook - Rs. 127.50
# Regular Size Notebook - Rs. 41.40
# Write a Python program for Ryan, to calculate the total amount,and generate the bill for the customer.
pencils = 75
ball_pens = 30
long_notebook = 127.50
medium_notebook = 41.40
pack_pencils = int(input("How many pack of pencils do you want"))
pack_pens = int(input("How many pack of ballpoint pens do you want"))
long = int(input("How many long copies do you want"))
medium = int(input("How many pack of regular size copies do you want"))
pencils = pencils * pack_pencils
pens = ball_pens * pack_pens
long = long * long_notebook
medium = medium * medium_notebook
total = pencils + pens + long + medium
print(pencils)
print(pens)
print(long)
print(medium)
print()
print(total)





"""-----------Task 3: Speed Conversion ------"""
print(" ")
print("*** Task 3: ***")
# Write a program to convert the speed from km/hr to m/s
# [Hint:To convert km/hr into m/sec, multiply the number by 5 and then divide it by 18.]
km = int(input("Enter the speed in km"))
km = km * 5
m = km/18
print("The same value in m/s is",m)



"""-----------Task 4: Area and Perimeter of Circle ------"""
print(" ")
print("*** Task 4: ***")
#Write a program to accept the radius of a circle, and calculate its area and perimeter. 
#[Hint:Area = 3.14 * (radius) to power of 2    and  Perimeter = 2*3.14*radius]
radius = float(input("Enter the radius of the circle"))
area = 3.14 * radius ** 2
print("The area of the circle is ",area)
perimeter = 2 * 3.14 * radius
print("The perimeter of the circle is ",perimeter)


input()


'''Awesome! You are becoming a pro in Python programming.You are mastering the use of data types in solving arithmetic problems'''
