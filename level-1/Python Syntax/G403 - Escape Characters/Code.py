# Program ID: G403
# Exercise Type: String Formatting using Escape Characters
# Tasks Included:
# - Task 1: Use newline (\n) to format multi-line output
# - Task 2: Create graphical patterns using \n and \t

# Original code starts below

# Level 1
# Part 1: Python Syntax
# G403 - Escape Characters
# You have learnt integers and float data type. 
# Shall we try some simple hacks to work with String data type.
# Let's get started!!
"""-----------Task 1:  Lets Escape!! ---------------"""
print(" ")
print("*** Task 1: ***")
# Suppose  you want to print a long sentence on the screen, like the one below:
# "Hello this is a long sentence and I want it to be visible to me as a paragraph because writing such long sentences is fun"
# What would you do? 
# It's pretty straightforward. You would use the print() statement.
# If I want you to print the same sentence  as follows:
# Hello
# This is a long sentence
# And I want it to be visible to me
# As a paragraph
# Because
# Writing such long sentences
# Is
# Fun
# Can you do it? 

# One way to get the output, is to use multiple print statements like:
#print("Hello")
#print("This is a long sentence")
#print("And I want it to be visible to me")
# And so on…
print("Hi\nI am a human \nI study \nI like to code and read\nMy favourite hobby is to read story books")
# What if I say there is a hack to achieve it in a single print statement. 
# Eager to know!!
# All you have to do is insert "\n" wherever you need a newline to appear.
# Uncomment the statement and click run:
#print("Hello \nThis is a long sentence \nAnd I want it to be visible to me \nAs a paragraph \nBecause \nWriting such long sentences \nIs \nFun")
# Did you notice that you got the output in multiple lines, and nowhere was the \n  printed.
# The character "\" is called the escape character and "n" means a new line.
# Uncomment the below statement and Click on Run:
#print("Hissing \tAway \tWriting \tPython \tProgram")
# What is the output you have gotten?
# Did you get this output with each word spaced away?
# Here "\t" inserts a tab. A tab inserts blank spaces between two words.
# It is similar to pressing the <Tab> key on your keyboard, when typing in a Word document. 
# If I want a line printed as below:
# I am studying about \n in the class
# Do you think the print statement below will give the result? Lets try
# Uncomment the below statement and click on Run:
#print("I am studying about \n in the class")
# Is \n getting printed in the output?  

# The reason is because when Python sees \n, it thinks it needs to insert a new line.
# We need to tell Python to print \n as is.
# To do so we include another \ before \n
# Python  prints whatever is after the backslash (\) as it is, without any changes 
# Lets try. Uncomment the line below and click Run:
#print("I am studying about \\n in the class")
#Does it work? Absolutely it does. 

"""-----------Task 2:  Graphical Escape!! ---------------"""
print(" ")
print("*** Task 2: ***")
# It is time to get creative.
# Using the escape character you have learnt in Task 1, can you build a graphic image and give it a name.
# Remember to use both \t and \n
print("*\n*\t*\t*\n*\t*\t*\t*\t*")
print("\t\t*\n\t*\t*\t*\n*\t*\t*\t*\t*\t*")
