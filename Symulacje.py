#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har
from Algorytmy import LeapFrog as LP
from Uklad import Uklad
from Kulka import Kulka

class Symulacje():
    def __init__(self, uklad, potencjal, algorytm, steps = 10):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__steps = steps
        
    def run(self):
        lista_kul = self.__uklad.kulka_get
        for i in range(self.__steps):
            f = self.__potencjal.calc_forces(lista_kul[0], lista_kul[1])
            for i in range(len(lista_kul)):
                algo = self.__algorytm.ruch(f, lista_kul[i])
                self.__algorytm.update_pos(algo[0], lista_kul[i])
                self.__algorytm.update_ver(algo[1], lista_kul[i])
        
        # testtuje
        return 'nowa pozycja'
    
if __name__ == "__main__":
    kulka1 = Kulka([0], 1, [0])
    kulka2 = Kulka([1], 1, [0])
    kulki = [kulka1, kulka2]
    uklad = Uklad(kulki)
    potencjal = Har()
    algorytm = LP()
    s = Symulacje(uklad, potencjal, algorytm)
    print(s.run())
    a1 = uklad.kulka_get[0].pos_get_all
    a2 = uklad.kulka_get[1].pos_get_all
    print(a1, a2)