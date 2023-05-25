# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:35:23 2022

@author: Márton
"""

def kame_hame():
    for i in range (1,411):
        if i % 4 == 0 and i % 10 == 0:
            print("Kame Hame!")
        elif i % 4 == 0:
            print("Kame!")
        elif i % 10 == 0:
            print("Hame!")
        else:
            print(i)
            
kame_hame()