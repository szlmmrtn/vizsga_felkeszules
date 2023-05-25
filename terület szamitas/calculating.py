# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:35:23 2022

@author: Márton
"""

class calculating:
    def __init__(self, number1, number2):
        self.number1 = int(number1)
        self.number2 = int(number2)
        self.kerulet = 0
        self.terulet = 0
    def calculating(self):
        self.kerulet = 2*(self.number1+self.number2)
        self.terulet = self.number1 * self.number2
        
        