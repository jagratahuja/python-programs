# Program ID: G302
# Exercise Type: Operator Precedence (BODMAS) and Arithmetic Applications
# Tasks Included:
# - Task 1: Demonstrate arithmetic expressions with and without parentheses
# - Task 2: Calculate total and average marks from user input
# - Task 3: Grocery billing calculation with a 10% discount

# Original code starts below

# Level 1
# Part 1: Python Syntax
# G302 - BODMAS
''' Task 1: '''
print(" ")
print("***** Task 1: *****")

p=6 + 10 / 2
q=(6 + 10) / 2
r=2 + 3 * 5
s=(2 + 3) * 5
t=6 +(8 / 4) - 2 * 3
v=(6 + (8 / 4) - 2) * 3
print(p)#11
print(q)#8
print(r)#17
print(s)#25
print(t)#2
print(v)#18


''' Task 2: '''
print(" ")
print("***** Task 2: *****")

english=int(input("what is your english score?"))
science=int(input("what is your science score?"))
math=int(input("what is your math score?"))
comp_science=int(input("what is your computer science score?"))
history=int(input("what is your history score?"))
print("Total Marks Scored = ",english + science + math + comp_science + history)

print((english + science + math + comp_science + history) / 5)

''' Task 3: '''
print(" ")
print("***** Task 3: *****")

cauliflower=int(input("how many kg you want of cauliflower"))

potato=int(input("how many kg you want of potato"))
      
beans=int(input("how many kg you want of beans"))
     
onion=int(input("how many kg you want of onion"))

total = (potato * 15) + (cauliflower * 30) + (onion * 20) + (beans * 25)

print(total)
print(90 * total/100)

'''
Ready for a role play?

You work at the "Freshmart Grocery Shop" as an accountant.

Your manager has given you the following rate card:

1 kg of cauliflower - Rs. 30
1 kg of potato - Rs. 15
1 kg of Onion - Rs. 20
1 kg of Beans - Rs 25
This week happens to be the discount week for customers.

You need to give the customer a discount of 10% on the total purchase.

You have a customer who has bought:

2 kg of potato
1 kg of onion
1 kg of beans
2 kg of cauliflower
Write a Python program to calculate the amount the customer needs to pay.
'''
