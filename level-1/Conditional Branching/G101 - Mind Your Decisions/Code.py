# Program ID: G101
# Exercise Type: Conditional Branching (if-else)
# Tasks Included:
# - Task 1: Decision making based on yes/no input
# - Task 2: Evaluate boolean expressions using comparison operators
# - Task 3: Compare two numbers to find the greater value
# - Task 4: Check if a frame is square or rectangular

# Original code starts below

# Level 1
# Part 2 Conditional Branching
# G101 - Mind Your Decisions

# Answer the below questions either with a Yes or a No
# Are you a June born?
# Do you like Harry Potter books?
# Do you have a sibling?
# How did you decide on the response? 
# You knew for the questions asked, the answer was either true (yes) or false. (no).
# Can computers also decide things for us? Wonder how ?
# Let's test it out.

"""-----------Task 1:  A Yes or A No ---------------"""
print(" ")
print("*** Task 1: ***")
# Uncomment the statements and click Run
print ("You have entered the Haunted Game Room")
print ("Do you see a spooky figure?")
answer = input("Type yes or no and hit 'Enter'.")
if answer == "yes":
 print ("You are entering the Jumpscare Mansion!! your spooky friends are ready to surprise you")
else :
 print ("You are entering the Haunted Mansion garden!! Beware of the purple flowers!")

# What happened when you typed yes or no? 
# Hence you can write programs and perform actions based on decisions.
# Ready to take the first step.

"""-----------Task 2:  Comparison Feat ---------------"""
print(" ")
print("*** Task 2: ***")
# Let’s start with the first step in evaluating a decision.
# Uncomment the statement below and click Run
#print (bool(2 == 5))
# What output did you get?
# The bool() function is used to check if a condition is true or false
# In the statement you just executed, the bool() function checks if 2 is equal to 5 using the “==” operator.
# The "==" compares whether 2 and 5 are equal. Since they are not it returns false.
# The "==" operator is called a comparator.
# Ready to try some more comparators. Uncomment the statements below and click Run.
print("***Statement 1***")
print (bool(2 == 2))#true
print("***Statement 2***")
print (bool( 2 != 5))#t
print("***Statement 3***")
print (bool( 5 < 2))#f
print("***Statement 4***")
print (bool( 2 <= 2))#t
print (bool(5 <= 2))#f
print("***Statement 5***")
print (bool( 5 > 2))#t
print("***Statement 6***")
print (bool( 5 >= 5))#t
print (bool(2 >= 5))#f

# Can you tell me what each statement is doing?
# Remember: Comparisons result in either True or False, which are boolean values


"""-----------Task 3:  Test the Condition ---------------"""
print(" ")
print("*** Task 3: ***")
# Ready to try out your first program to test a condition.
# Uncomment the statements and click on Run
a=input("Enter a number:")
b=input("Enter another number: ")
if a>b:
  print("The greater of the two numbers is: ", a)
else: 
  print("The greater of the two numbers is: ",b)

# What does the program do? 
# The program accepts two numbers from the user. 
# It checks if the first number is greater than the second
# If yes, it prints it as the greater.
# If not, it prints the second number as the greater.
# Let us look at how the if statement works.
# if <condition is true>:
#    <set of actions to perform for true condition>
# else:
#   <set of actions to perform for false condition>

# You must remember the following: 
# The if and the else statement end with a colon (:)
# Leave three spaces and start typing the statements after the if  statement in the next line (indentation) 
# Similarly type the statements after the else statement in the next line after leaving three spaces (indentation) 
# You must include a colon (:) at the end of each if, and else statement, which tells Python to automatically indent the following line.
# If you do not follow the above mentioned points you will get an error [Must Say]

"""-----------Task 4:  Whats in a frame? ---------------"""
print(" ")
print("*** Task 4: ***")
# The program below asks the user to enter the length and breadth/width of a photo frame.
# If both the length and width are equal, the program prints "The photo frame is a square"
# If not  it prints "The photo frame is a rectangular"
# Uncomment the statements below, write the code for the if and the print statements. [Hint: Use the == comparator]
# Click Run to display the output
a=input("Enter the length of the photo frame: ")
b=input("Enter the breadth of the photo frame : ")
if a==b:
  print("It is a square")
else: 
  print("It is a rectangle")
