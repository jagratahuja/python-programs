# Program ID: G404
# Exercise Type: String Operations and Operator Behavior
# Tasks Included:
# - Task 1: Demonstrate how + and * behave with strings and numbers
# - Task 2: Use input with string concatenation and repetition

# Original code starts below

# Level 1
# Part 1 Python Syntax
# G404 - Python Mysteries
# Are you ready to witness some Python mysteries.Lets check it out.
"""-----------Task 1:  What's in store? ---------------"""
print(" ")
print("*** Task 1: ***")
#By now you are aware of the different arithmetic operators as well as the data types.
#Did you know when you use the '+' and '*' operators, Python decides to treat the strings differently. 
#And the output you get is also different.
#Let's take a look. Uncomment the statements below and click Run.
print(1+2)#3
print("1"+"2")#12
print("robin" +"hood")#robinhood
print(2*2)#4
print(2*"hello")#hellohello
# Did you see the output? Why do you think that happened? 
# When an arithmetic operator is used with strings, it processes them differently. 
# With the "+" operator  strings are combined
# With "*" operator a string is replicated  or repeated 
# For example (Uncomment to check):
#print(2*"welcome") will print “welcome” twice
#print("I am enjoying " +"programming with " +"Python") will print “I am enjoying programming with Python”

"""-----------Task 2:  Test it Out ---------------"""
print(" ")
print("*** Task 2: ***")
# Ready for a small challenge?
# The following text should be displayed using the “+” and “*” operators:
# Welcome to class <user>  
# Enjoy Python!Enjoy Python!
# [Hint: You need to get the name from the user]
# Write a python program to display the output
name = input("Enter your name : ")
print("Welcome to class ",name)
print(2*"Enjoy Python!")



'''That was brilliant. You really put on your thinking hat. Way to go!!'''
