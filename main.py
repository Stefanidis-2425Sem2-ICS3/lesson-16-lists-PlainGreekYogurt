# Name: Malaki S.
# Title: List of numbers
# Date: March 24th, 2025
# Description: This program makes a list of 100 random numbers, then finds the average of them.


import random
number = []
for index in range (1 , 100):
    num = random.randint (1 , 100)
    print (num)
    number.append (num)
average =(sum(number)/100)
print ("The average is" , average)