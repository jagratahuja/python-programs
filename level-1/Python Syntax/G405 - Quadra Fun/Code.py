# Program ID: G405
# Exercise Type: Geometry and Cost Calculation
# Tasks Included:
# - Task 1: Calculate perimeter of a rectangular field and area of a hockey pitch
# - Task 2: Compute worker wages and total payment

# Original code starts below

# Level 1
# Part 1 Python Syntax
# G405 - Quadra Fun
'''
Quadra Fun
You are a part of the sports committee in your apartment complex.

The committee head wants your help in developing a rectangular piece of land into a playground.

Are you ready to use your Python programming skills in solving the issue ?

 

Task 1: Getting the Sports Field Ready

The Committee Head wants to convert a rectangular piece of land which is 118.5 meters long and 67.5 meters wide into a sports field.

You and your friends propose the idea of splitting the land into a football pitch and hockey pitch with the following measurements:

91.5m long and 55m wide [football pitch]
27 m long and 20.5 m wide [hockey pitch]
The Committee head loves the idea. He decides to:

First fence the sports field first and then
Put artificial grass/turf for the hockey pitch.
He asks you to give the measurement for both so that he can get the materials.

You decide to write a Python program to calculate the measures.

So why wait, get programming!!

Hint: For fencing, you need to get the perimeter of the sports field which is rectangular ( formula: perimeter - 2(length + width))
Hint: For the artificial turf/grass, you need to get the area of the rectangular hockey pitch (Area = length * width]
 

Task 2: How much do we pay?

The Committee Head is very happy with your program and calculation.

Now they want your help in calculating how much needs to be paid to the workers who will be laying the fence and artificial turf/grass.

Two workers will be helping with this task.

For an hour of work, each of them gets paid Rs. 150.
To finish the job, each worker will take about 8.5 hrs.
So you need to calculate the total amount to be paid to each worker and the total cost

Write a python program to calculate the amount.


'''


l1 = 118.5
w1 = 67.5

l2 = 27
w2 = 20.5

p1 = 2 * (l1 + w1)
a1 = l2 * w2

print("Task 1: Getting the Sports Field Ready")
print("Perimeter of sports field (for fencing):", p1, "meters")
print("Area of hockey pitch (for artificial turf):", a1, "sq. meters")



n = 2
r = 150
h = 8.5

ppw = r * h
tp = ppw * n

print("\nTask 2: Worker Payment")
print("Amount to be paid to each worker: Rs.", ppw)
print("Total amount to be paid to all workers: Rs.", tp)
