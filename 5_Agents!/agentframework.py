#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:43:11 2021

@author: maryamali
"""

import random

class Agent ():
    
    def __init__ (self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
        
# Make a move() method with the Agent Class
     
    def move(self):
        if random.random() < 0.5:
             self.y = (self.y + 1) % 100
        else:
             self.y = (self.y - 1) % 100

        if random.random() < 0.5:
              self.x = ( self.x + 1) % 100
        else:
              self.x = (self.x - 1) % 100