# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:35:23 2022

@author: Márton
"""
from calculating import calculating
import datetime


x = datetime.datetime(2022, 1, 3)
class printing:
    def __init__(self, username, num1, num2):
        self.username=username
        self.number1 = int(num1)
        self.number2 = int(num2)
    def nyomtatos_funkcio(self):
        self.ez = calculating(self.number1,self.number2)
        self.ez.calculating()
        
        f = open("Szamitasoslap.txt","w")
        f.write("Számításos lap")
        f.write("\n")
        f.write(f"felhasználó neve: {self.username}")
        f.write("\n")
        f.write(f"Egyik oldal hossza: {self.number1}")
        f.write("\n")
        f.write(f"felhasználó neve: {self.number2}")
        f.write("\n")
        f.write(f"Kerület: {self.ez.kerulet} m")
        f.write("\n")
        f.write(f"Terület: {self.ez.terulet} m2")
        f.write("\n")
        f.write("\n")
        f.write(f"kelt: Szeged, {x}")
        