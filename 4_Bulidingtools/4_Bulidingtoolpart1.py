#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:06:52 2021

@author: maryamali
"""

import random
import operator
import matplotlib.pyplot


num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

def distance_between (a,b):
    """
    This function calculates
    and returns the distance between a & b

    Parameters
    ----------
    a : This is a list with two elements that are both numbers
        Coordinates 
       
    b : This is list with two elements that  are both numbeers 
        Coordinates

    Returns
    -------
    Float 
        Pythagoran distance in 2D between a and b

    """

    return ((( a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5

#Calcuate the distance 
#Calcuate the maximum and minimum distance
#Max_dist = (((agents[0][0] - agents[1][0])**2)
#          + ((agents[0][1] - agents[1][1])**2))**0.5
max_dist = distance_between(agents[0], agents[1])
min_dist = max_dist
for i in range(num_of_agents):
    for j in range(num_of_agents):
        # answer = (((agents[i][0] - agents[j][0])**2)
        #         + ((agents[i][1] - agents[j][1])**2))**0.5
        answer = distance_between(agents [i], agents[j])
        max_dist = max(max_dist, answer)
        min_dist = min(min_dist, answer)
        print(answer)
        print ("max_dist", max_dist)
        print ("min_dist", min_dist)



matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

