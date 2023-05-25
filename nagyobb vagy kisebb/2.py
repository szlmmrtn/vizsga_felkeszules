# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:56:21 2021

@author: Márton
"""
import random

game_on = True
life = 3
gen_num = random.randint(50,55)

def guessing_game(guess_num, gen_num):
    global life
    global game_on
    if guess_num == gen_num:
        print("Nyertél barátom!")
        game_on = False
    else:
        if guess_num > gen_num:
            print("kisebb")
            life -= 1
        elif guess_num < gen_num:
            print("nagyobb")
            life -= 1
    

while game_on:
    inp_num = input("Találd ki a számot(50-55) ")
    if inp_num.isnumeric() and (int(inp_num) > 49 and int(inp_num) < 56):
        guess_num = int(inp_num)
        guessing_game(guess_num, gen_num)
    elif life == 0:
        print("Vesztettél lúzer!")
        game_on = False
    else:
        life -= 1
        print("kérek egy számot 50 és 55 között! ")