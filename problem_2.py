#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:25:19 2018

@author: Rohit Swami

Question:
Ten students (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10) are going to attend an event. 
There are lots of gift shops, they all are going to the gift shops and randomly
 picking the gifts. After picking the gifts they are randomly arriving in the
 billing counter. The accountant gives the preference to that student who has 
 maximum number of gifts. Create a C program to define order of billed 
 students?
"""

import random

# Desclaring a list
s=[]

# Populating list with random numbers (gifts)
for i in range(10):
    a = random.randint(1, 20)
    if a not in s:
        s.append(a)
print(s)




















































































