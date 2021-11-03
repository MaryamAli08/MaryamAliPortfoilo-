#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:42:40 2021

@author: maryamali
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

# Install environment as a list of list
environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            #print(value) 
            rowlist.append(value)
        environment.append(rowlist) 

# To check if it works, print enviroment 
print(environment) 

rows = len(environment)
cols = len(environment[0])
print("rows", rows)
print("cols", cols)

# To check if each of the rows have the same number columns
for rows in range(rows):
    if (len(environment[rows]) != cols):
        print("unhappy")
    # else :
    #     print("unhappy")
        
# #visualisation
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()


def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.x - agents_row_b.x)**2) + 
     ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 10
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents,environment))
    random.shuffle(agents)
# Move the agents.
#Shuffle the agents
for j in range(num_of_iterations):
    print("Iteration", j)
    #random.shuffle(agents)
    for i in range(num_of_agents):
         print(agents[i])
         # print(i, "before move", agents[i].x, agents[i].y)
         agents[i].move()
         # print(i, "after move", agents[i].x, agents [i].y)
         # print("store before eat", agents[i].store)
         agents[i].eat()
         # print("store after eat", agents[i].store)
         agents[i].share_with_neighbours(neighbourhood)
        
         
matplotlib.pyplot.imshow(environment)         
matplotlib.pyplot.xlim(0, cols )
matplotlib.pyplot.ylim(0, rows)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
     for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
        
#Can you override __str__(self) in the agents

#print agents 
for i in range(num_of_agents): 
    print(agents[i])
    print("Final agents")
    