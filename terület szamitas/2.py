# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:35:23 2022

@author: Márton
"""

import random

game_on = True
life = 4
gen_num = random.randint(100, 110)

def talaldki_game(guess_num):
    global gen_num
    global life
    global game_on
    if gen_num == guess_num:
        print("Nyertél haver!")
        game_on = False
    else:
        life -= 1
        if gen_num > guess_num:
            print("nagyobb!")
        elif gen_num < guess_num:
            print("kisebb!")
        

while game_on:
    if life >= 0:
        guessnum = input("Találd ki a számot (100-110) ! ")
        print(life)
        if guessnum.isnumeric:
            if int(guessnum) > 100 and int(guessnum) < 110:
                guess_num= int(guessnum)
                talaldki_game(guess_num)
            else:
                print("Nem 100 és 110 között adtál meg!")
                life -= 1
        else:
            print("Nem számot adtál meg!")
            life -= 1
    else:
        game_on = False
        print("Béna vagy!")


