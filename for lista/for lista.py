# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:55:04 2021

@author: Márton
"""

size_input = input("Mekkora legyen a lista? ")
if size_input.isnumeric():
    size = int(size_input)
    lista = [size]
    for i in range(0,size):
        input_lista = input(f"Add meg a lista {i} tagját: ")
        lista.append(input_lista)
else:
    print("Számot adj meg")

