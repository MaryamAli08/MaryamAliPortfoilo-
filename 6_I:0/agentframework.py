#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:43:11 2021

@author: maryamali
"""

import random

class Agent ():
    
    def __init__ (self, environment):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0 
    #To return a string representation of our agents
    def __str__(self):
        return "x=" + str(self.x) \
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
          
           
           
           
           
           