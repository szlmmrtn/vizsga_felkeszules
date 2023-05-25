# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:56:21 2021

@author: Márton
"""
from calculating import calculating

class printing:
    def __init__(self, username, number):
        self.us = username
        self.numb = number
        
        
    def printer(self):
        self.ez = calculating(self.numb)
        self.ez.calculate()
        f = open("Szamitasoslap.txt","w")
        f.write("Számításos lap")
        f.write("\n")
        f.write(f"Felhasználó neve: {self.us}")
        f.write("\n")
        f.write(f"Bekért szám: {self.numb}")
        f.write("\n")
        f.write(f"Tripla: {self.ez.dupla}")
        f.write("\n")
        f.write(f"Dupla: {self.ez.tripla}")
        f.write("\n")
        f.write("\n")
        f.write("Kelt: Szeged,2021.12.15")
        f.close