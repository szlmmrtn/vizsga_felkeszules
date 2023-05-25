# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:56:21 2021

@author: Márton
"""

def fus_rodah():
    for n in range (1, 351):
        if n % 2 == 0 and n % 11 == 0:
            print("Fuss rodah!")
        if n % 2 == 0:
            print("Fuss")
        if n % 11 == 0:
            print("Rodah")
        else:
            print(n)
            
fus_rodah()