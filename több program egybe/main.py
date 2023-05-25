# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:56:21 2021

@author: Márton
"""
from printing import printing


username = input("Kérem a felhasználóneved! ")
number = input("Kérem a számot! ")
if number.isnumeric():
    fajlbairas = printing(username, number)
    fajlbairas.printer()
else:
    print("Számot adj meg!")