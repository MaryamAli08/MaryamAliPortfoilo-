#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: maryamali
"""

import random


# Make a y variable.
y0 = 1
# Make a x variable.
x0 = 1
# Change y and x based on random numbers.
# import random

#change y0

random_number = random.random()
print("random_number" , random_number)
if random_number < 0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
    
print("y0", y0)
  
# change x0 
  
random_number = random.random()
print("random_number" , random_number)

if random_number < 0.5:
    
    x0 = x0 + 1
else: 
    x0 = x0 - 1

print("x0", x0)

#Make a second set of y and xs, and make these change randomly as well


# Two points needed

x1 = 0
y1 = 0

# change y1 

random_number = random.random()
print("random_number" , random_number)
if random_number < 0.5:
    
    y1 = y1 + 1
    
else: 
    y1 = y1 - 1
    
print("y1", y1)
  
# change x1 
  
random_number = random.random()
print("random_number" , random_number)

if random_number < 0.5:
    
    x1 = x1 + 1
else: 
    x1 = x1 - 1

print("x1", x1)

# this is a test for distance

x0 = 0
y0 = 0
x1 =1
y1 = -1

#Work out the distance between the two sets of y and xs.


Distance = ((y0 - y1) * (y0 - y1) + (x0 - x1) * (x0 - x1))**0.5
print ("Distance", Distance)











