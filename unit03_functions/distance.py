#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 08:15:15 2020

@author: claus
"""

from numpy import *

distance=[[0, 20, 30, 40],
          [20, 0, 50, 60],
           [30, 50,0,70],
           [40, 60, 70, 0]]

n = len(distance)

red_distance=[]

for row in range(1,n):
    red_row=[]
    for col in range(row):  # stops at row-1
         red_row.append(distance[row][col])
    red_distance.append(red_row)     
    
    
# Alternative 2
red_row=[]
red_distance2=[red_row.append(distance[row][:row]) for row in range(1,n)] 

# Alternative 3

red_distance3=[distance[row][:row] for row in range(1,n)] 