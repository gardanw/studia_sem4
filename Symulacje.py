#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Potencjal
from Algorytm import Algorytm
from Uklad import Uklad

class Symulacje():
    def __init__(self, uklad, potencjal = Harmoniczny(), algorytm = Leap_frog(), dt=0.1, steps = 10):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__dt = dt
        self.__steps = steps
        
    def run(self):
        pass
if __name__ == "__main__":
    s = symulacja(uklad = Uklad(kulki))