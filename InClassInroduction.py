#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:09:54 2021

@author: rh.hayden
Title: Python Introduction
"""

# Hash tag can be used for commenting
""" anything between 3 double quotes is a comment as well """

# No required semicolons
print("Hello. This is your introduction to Python")

# Can use if and elif
# Tabs matter
if 10 < 2:
    print("10 is not less than 2")
    print("Conversely, 2 is not greater than 10")
else:
    print("2 is less than 10")
    
# Assigning variables
age = 21
name = 2
print(age + name)

name = "Roger" # This will not consider name to be a string
print("My name is " + name + ".")

firstName, middleName, lastName = "Roger", "Henry", "Hayden III"
fullName = ("Roger", "Henry", "Hayden III") # This will create an array of strings

# Indexing starts at 0 in Python
print(fullName[0] + " " + fullName [1] + " " + fullName [2])
print("Your full name has " + str(len(fullName)) + " parts.")

# You can force variable types - Casting
speed = float(65.0)
speed2 = int(66)

#You will need to use a function if you wish to combine a numeric and string output
#Python does not like mixing variables - It is object oriented
print(name + " is " + str(age) + " years old.")

#If you need to use a random number
import random # This can be imported any time before you use it

randomNumber = random.randrange(1, 100)
print("Your random number is: " + str(randomNumber))

# Basic loop structures work as in many other languages
# Loops are designed in a data/analysis perspective
# Still can be used as a menu loop

# This loops through the contents in an array
for x in fullName:
    print(x)
    
for x in range(1, 7):
    print("Number X is " + str(x))
  
# Creates infinite loop if y > 0
y = 0
while y > 10:
    print("Number Y is " + str(y))
    y+=1
    
#You can create functions to utilize over and over again
#Note the separate two lines
def calculate(s, t):
    print("The total is " + str(s * t))
    
# Now that my function is created, I can call it and pass in values
calculate(10,16)