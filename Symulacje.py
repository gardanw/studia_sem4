#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har
from Algorytmy import LeapFrog as LP
from Uklad import Uklad
from Kulka import Kulka

class Symulacje():
    def __init__(self, uklad, potencjal, algorytm, dt=0.1, steps = 10):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__dt = dt
        self.__steps = steps
        
    def run(self):
        lista_kul = self.__uklad.kulka_get
        x = self.__potencjal.calc_forces(lista_kul[0], lista_kul[1])
        # testtuje
        return x
    
if __name__ == "__main__":
    kulka1 = Kulka([0], 1, [0])
    kulka2 = Kulka([1], 1, [0])
    kulki = [kulka1, kulka2]
    uklad = Uklad(kulki)
    potencjal = Har()
    algorytm = LP()
    s = Symulacje(uklad, potencjal, algorytm)
    print(s.run())