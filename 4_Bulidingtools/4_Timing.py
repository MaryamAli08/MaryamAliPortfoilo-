#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:14:29 2021

@author: maryamali
"""

import random
import operator
import matplotlib.pyplot
import time

# Start the clock ()
start = time.time()
#start = time.time()



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

def calcuate_distance0(agents):
    print("calcuate_distance0")
    start0 = time.time()
    #Calcuate the distance 
    # Calcuate the maximum and minimum distance
    # Max_dist = (((agents[0][0] - agents[1][0])**2)
    #          + ((agents[0][1] - agents[1][1])**2))**0.5
    max_dist = distance_between(agents[0], agents[1]) 
    min_dist = max_dist
    for i in range(0, num_of_agents, 1):
        #for j in range (i , num_of_agents,1)
        for j in range(0, num_of_agents, 1):
            if i < j:
               #if i != j:
               #print(i,j)
               # answer = (((agents[i][0] - agents[j][0])**2)
               #         + ((agents[i][1] - agents[j][1])**2))**0.5
               answer = distance_between(agents [i], agents[j])
               max_dist = max(max_dist, answer)
               min_dist = min(min_dist, answer)
               #print(answer)
               #print ("max_dist", max_dist)
               #print ("min_dist", min_dist)
               # if answer == 0.0:
               #     print("i" ,i)
               #     print("j", j)
               #     print("agents[i]", agents [i])
               #     print("agents[j]", agents [j])
    end0 = time.time()          
    print ("time = " + str(end0 - start0)) 
    print ("max_dist", max_dist)
    print ("min_dist", min_dist)
    return end0 > start0
         
def calcuate_distance1(agents):
      print("calcuate_distance1")
      start1 = time.time()
      #Calcuate the distance 
      # Calcuate the maximum and minimum distance
      # Max_dist = (((agents[0][0] - agents[1][0])**2)
      #          + ((agents[0][1] - agents[1][1])**2))**0.5
      max_dist = distance_between(agents[0], agents[1]) 
      min_dist = max_dist
      for i in range(0, num_of_agents, 1):
          #for j in range (i , num_of_agents,1)
          for j in range(0, num_of_agents, 1):
              if i < j:
               #if i != j:
               #print(i,j)
               # answer = (((agents[i][0] - agents[j][0])**2)
               #         + ((agents[i][1] - agents[j][1])**2))**0.5
               answer = distance_between(agents [i], agents[j])
               max_dist = max(max_dist, answer)
               min_dist = min(min_dist, answer)
               #print(answer)
               #print ("max_dist", max_dist)
               #print ("min_dist", min_dist)
               # if answer == 0.0:
               #     print("i" ,i)
               #     print("j", j)
               #     print("agents[i]", agents [i])
               #     print("agents[j]", agents [j])
      end1 = time.time()          
      print ("time = " + str(end1 - start1)) 
      print ("max_dist", max_dist)
      print ("min_dist", min_dist)
      return end1 > start1
 
# Number of agents below

timings0 = []
timings1 = []
for num_of_agents in range (100, 1000, 100):
    print ("num_of_agents", num_of_agents)
    #num_of_iterations = 100
    agents = []
    # Make the agents.
    for i in range(num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])
    

    timings0.append(calcuate_distance0(agents))
    timings1.append(calcuate_distance1(agents)) 
       
print("timings0", timings0)
print("timings1", timings1)

max_time = max(timings0)
max_time = max(max_time,max(timings1))
               
#stop the timing and print time
end = time.time()

print ("time = " + str (end - start))    

#plot the agents
matplotlib.pyplot.ylim(0, 1000)
matplotlib.pyplot.xlim(0, max_time)
i = 0
for num_of_agents in range(100, 1000, 100):
    matplotlib.pyplot.scatter(timings0[i],num_of_agents, color= "red")
    matplotlib.pyplot.scatter(timings1[i],num_of_agents, color= "blue")
    i = i + 1
matplotlib.pyplot.show()



# '''
# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
#for j in range(num_of_iterations):
#  for i in range(num_of_agents):

#       if random.random() < 0.5:
#           agents[i][0] = (agents[i][0] + 1) % 100
 #       else:
  #          agents[i][0] = (agents[i][0] - 1) % 100

  #      if random.random() < 0.5:
  #          agents[i][1] = (agents[i][1] + 1) % 100
   #     else:
   #         agents[i][1] = (agents[i][1] - 1) % 100
