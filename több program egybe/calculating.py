# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 12:56:21 2021

@author: Márton
"""
class calculating:

    def __init__(self, number):
        self.num = int(number)
        self.dupla = 0
        self.tripla= 0
    def calculate(self):
        global dupla
        global tripla
        self.tripla = self.num * 3
        self.dupla = self.num * 2