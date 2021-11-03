#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:43:11 2021

@author: maryamali
"""

import random

class Agent ():
    
    def __init__ (self, i, agents, environment,rows, cols, y, x):
        #self.x = random.randint(0,99)
        #self.y = random.randint(0,99)
        self.x = x
        self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self.i = i 
        
    #To return a string representation of our agents
    def __str__(self):
        return "id=" + str(self.i) \
            + ", x=" + str(self.x) \
            + ", y=" + str(self.y) \
            + ", store=" + str(self.store)
    
    
# Make a move() method with the Agent Class
     
    # def move(self):
    #     if random.random() < 0.5:
    #          self.y = (self.y + 1) % 100
    #     else:
    #          self.y = (self.y - 1) % 100

    #     if random.random() < 0.5:
    #           self.x = ( self.x + 1) % 100
    #     else:
    #           self.x = (self.x - 1) % 100

# Make the agents wonder around the full environment         
              
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment )
        else:
            self.y = (self.y - 1) % len(self.environment )

        if random.random() < 0.5:
             self.x = ( self.x + 1) % len(self.environment[0])
        else:
             self.x = (self.x - 1) % len(self.environment[0])
              
# New function called 'eat'
# Adding a value less than to eat, without leaving negative values
    

    def eat(self):
       if  self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
       else:
           self.store += self.environment[self.y][self.x]
           self.environment[self.y][self.x]= 0
    def distance_between(self , b):
        return (((self.x - b.x)**2) + 
                ((self.y - b.y)**2))**0.5   
    
# Share neighbhours function 
     
    def share_with_neighbours(self,neighbourhood):
        # print ("neighbourhood", neighbourhood)
        # Loop through the agents in self.agents .
        #for agent in self.agents:
        for i in range (len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i]) 
            # If distance is less than or equal to the neighbourhood
            if distance < neighbourhood:
               print ("distance", distance)
        # Sum self.store and agent.store 
        sum = self.store + self.agents[i].store
        # Divide sum by two to calculate average.
        average = sum/2
        # self.store = average
        self.store = average
        # agent.store = average
        self.agents[i].store = average 
        # End if
        # End loop
           
           
           
           