# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:35:23 2022

@author: Márton
"""
from printing import printing

username = input("Kérem a neved! ")
num1 = input("Kérem a számot (1)! ")
if num1.isnumeric():
    num2 = input("Kérem a számot (2)! ")
    if num2.isnumeric():
        fajlbairas = printing(username, num1,num2)
        fajlbairas.nyomtatos_funkcio()
    else:
        print("nem számot adtál meg!")
else:
    print("nem számot adtál meg!")




