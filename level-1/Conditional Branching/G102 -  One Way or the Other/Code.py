# Program ID: G102
# Exercise Type: Conditional Branching with Multiple Conditions
# Tasks Included:
# - Task 1: Check if a number is positive, negative, or zero
# - Task 2: Evaluate marks and give feedback
# - Task 3: Check if a triangle is equilateral
# - Task 4: Determine which sides of a triangle are equal

# Original code starts below

# Level 1
# Part 2 Conditional Branching
# G102 - One Way or the Other
# If you had to evaluate multiple conditions, how would you do it? 
# Would the if statement handle multiple conditions?
# First let us look at single conditions again and then move to multiple conditions.

"""------Task 1:  Positive or Not --------"""
print(" ")
print("*** Task 1: ***")
# Write a program to take a number as an input from the user.
# Check if the number is positive or negative
number_1 = int(input("Write an Integer"))
if number_1<0 :
  print("It is a Negative Integer")
elif number_1>0 :
  print("It is a Positive Integer")
else :
  print("0 is neither a positive nor a negative integer")





"""-----Task 2:  What is your score? ---------"""
print(" ")
print("*** Task 2: ***")
# Write a program to get the marks for Mathematics from the user. 
# If the marks is less than 50, print a message saying “you need to improve”.
# If the mark is more than 50, print “ You are doing good. Keep it up!”
marks = int(input("Enter your Maths Marks"))
if marks<50 :
  print("You need to Improve")
else :
  print("You are doing good. Keep it up!")





"""------Task 3:  Is it an Equilateral Triangle --------"""
print(" ")
print("*** Task 3: ***")
# Do you know what an equilateral triangle is?
# If all the three sides of a triangle are equal, it's an equilateral triangle. 
# Here is a program to check if a triangle is equilateral.Uncomment the statements and click Run
a=input("Enter the first side of the triangle:  ")
b=input("Enter the second side of the triangle: ")
c=input("Enter the third side of the triangle: ")
if a != b:
 print( "It is not an equilateral triangle")
elif a==c:
 print("It is an equilateral triangle")
else:
 print("It is not an equilateral triangle")
if a==b==c :
  print("It is an Equilateral Triangle")
else :
  print("It is not an Equilateral Triangle")



# What do you think the program just did?
# The program checks if the three sides of the triangle are equal (multiple conditions).
# To check multiple conditions  the  “elif” clause has been used
# elif means "else if"
# So how has the if..elif..else been used in the program you just ran (the equilateral triangle program)? 
# The program checked the following conditions: 
# if side 1 is not equal to side 2.
# if it is true, then it means it is not an equilateral triangle
# if it is false, it means side 1 = side 2, so it checks if side 1 = side 3
# if it is true, then it is an equilateral triangle, else it is not
# Note: It is a good practice  to have the last statement as an else.




"""-----Task 4:  Which sides are equal? ---------"""
print(" ")
print("*** Task 4: ***")
# Can you modify the program you ran in Task 1 to check which two sides of the triangle are equal?
# [Hint: Use multiple elif statements]
a=input("Enter the first side of the triangle:  ")
b=input("Enter the second side of the triangle: ")
c=input("Enter the third side of the triangle: ")
if a==b==c :
  print("All sides are equal")
elif a==b :
  print("First and second side are equal")
elif a==c :
  print("First and third side are equal")
elif b==c :
  print("Second and Third side are equal")
else :
  print("No side is equal")
  

'''Kudos!! You handled multiple conditions effortlessly. Way to go!'''
