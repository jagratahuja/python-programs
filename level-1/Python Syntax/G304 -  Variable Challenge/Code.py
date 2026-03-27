# Program ID: G304
# Exercise Type: Variable Manipulation and Arithmetic Operations
# Tasks Included:
# - Task 1: Perform sequential arithmetic updates using multiple variables
# - Task 2: Modify a single variable through multiple arithmetic expressions

# Original code starts below

# Level 1
# Part 1: Python Syntax
# G304 - Variable Challenge
''' Task 1: '''
print(" ")
print("***** Task 1: *****")

first = 2
second = 3
third = first * second#6
second = third - first#4
first = first + second + third#12
third = second * first#48

print("First:", first)#12
print("Second:", second)#4
print("Third:",third)#48


''' Task 2: '''
print(" ")
print("***** Task 2: *****")

x = 10
x = x + x
x = x - 5
x = (x*5)/5 + 10
print("The value of x:",x)
