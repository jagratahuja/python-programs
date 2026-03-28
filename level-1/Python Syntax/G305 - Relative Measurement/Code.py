# Program ID: G305
# Exercise Type: Real-World Arithmetic Applications
# Tasks Included:
# - Task 1: Calculate cliff height using proportional shadow measurements
# - Task 2: Compute speeds of two cyclists and compare performance
# - Task 3: Calculate total distance, total time, and average speed

# Original code starts below

# Level 1
# Part 1: Python Syntax
# G305 - Relative Measurement
# Have you ever tried to measure a shadow? 
# Did you know you can measure larger objects like a cliff or a highrise building by measuring its shadow?

'''*****Task 1: Cliff Measure*****'''
print(" ")
print("*** Task 1:***")
# A rock climber wants to know the height of a cliff. 
# You need to write a program to help him calculate. 
# He shares the below information:
# The climber measures the shadow of her friend, who is 5 feet tall and standing beside the cliff 
# He then measures the shadow of the cliff.
# If the friend's shadow is 4 feet  long and the cliff's shadow is 60 feet long, how tall is the cliff?
# Hint: Cliff_height=friend_height * cliff_shadow / friend_shadow
friend_height = 5
friend_shadow = 4
cliff_shadow = 60
Cliff_height = friend_height * cliff_shadow / friend_shadow
print(Cliff_height,"feet")

'''*****Task 2: Fast and Furious*****'''
print(" ")
print("*** Task 2:***")
# Nathan and Ray decided to have a cycling competition on a Sunday. 
# They pulled out  their BTWin cycle and cycled to their favourite picnic spot l20kms from home. 
# Each of them decided to take a separate route to see who reaches faster. 
# Both started at 10:00am. 
# Nathan reached the picnic spot at 11:00am whereas Ray reached at 11:30am. 
# On his way Ray saw a beautiful bird and spent 15 minutes taking its photo.
# Write a Python program that calculates the speed at which each of them cycled and whose route was better.
# [Hint: Speed = Distance travelled/time taken]
distance = 120
time_1 = 60
time_2 = 75
speed_1 = distance/time_1
speed_2 = distance/time_2
print(speed_1,"km/per hour")
print(speed_2,"km/per hour")





'''*****Task 3: Challenge Galore*****'''
print(" ")
print("*** Task 3:***")
# After the cycling competition Nathan and Ray had on Sunday (as described in the previous task), they decided to take their challenge to the next level.
# They decided to cycle uphill and downhill on a hillock, close to home. 
# But this time they both went together. 
# Here are the details of the distance travelled:
# uphillDistance travelled: 10 km
# downhillDistance travelled: 9 km
# Time taken to go up hill: 66 minutes
# Time taken to come down hill: 46 minutes
# Write a program to calculate the total distance cycled and the average speed taken.
# [Hint: You need to find the total distance, the total time and then calculate the average speed as total distance/total time]
uphillDistance = 10
downhillDistance = 9
timeup = 66
timedown = 46
totaldistance = (uphillDistance + downhillDistance) 
print(totaldistance)
total_time = (timeup + timedown)
print(total_time)
average_speed = (totaldistance/total_time)
print(average_speed)
input()
