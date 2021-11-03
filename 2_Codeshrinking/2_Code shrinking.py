#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:26:21 2021

@author: maryamali
"""

import random
import operator  
import matplotlib
import matplotlib.pyplot






# Create a new empty list we can add sets of coordinates to
agents = []
agents.append([random.randint(0,99), random.randint(0,99)])

agents.append([random.randint(0,99),random.randint(0,99)])



# Change y and x based on random numbers.
# import random
random_number = random.random()

print ("random_number" , random_number)
if random_number < 0.5:
    agents[0][0]= agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

print ("y0" , agents[0][0])

random_number = random.random()
print ("random_number" , random_number)
if random_number < 0.5:
   agents[0][1] = agents[0][1] + 1
else:
   agents[0][1] = agents[0][1] - 1

print ("x0" , agents[0][1] )

#Then, after the making of y0 and x0, add:

# Print agents

print (agents)
for i in range (len (agents)) :
   print (agents[i])

# Print Maximum 

print ("Maximum", max (agents))
print ("Maximum item 1", max (agents, key=operator.itemgetter(1)))


# Make a second set of y and xs, and make these change randomly as well.

x1 = 0
y1 = 0


# change y1 

random_number = random.random()
print ("random_number" , random_number)
if random_number < 0.5:
  
    y1 = y1 + 1
else:
    y1 = y1  - 1

print ("y1" , y1)

# change x1

random_number = random.random()
print ("random_number" , random_number)
if random_number < 0.5:
  
    x1 = x1 + 1
else:
    x1 = x1  - 1

print ("x1" , x1)

# Lets add the second agent to the list 



# Check the length of the list
print("len (agents)", len (agents))
print (agents)


# Work out the distance between the two sets xs and Ys

Distance = ((agents[0][0]- agents[1][0]) * (agents[0][0]- agents[1][0]) + (agents[0][1] - agents[1][1]) * (agents[0][1] - agents[1][1]))**0.5
print ("Distance" , Distance)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)


matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#turn the top agent red
#turn the buttom agent pink

top = max (agents, key=operator.itemgetter(0))
matplotlib.pyplot.scatter (top[1], top[0], color = 'red')
    
buttom = min(agents, key=operator.itemgetter(0))
matplotlib.pyplot.scatter (buttom[1], buttom[0], color = 'pink')
                              

matplotlib.pyplot.show()

















