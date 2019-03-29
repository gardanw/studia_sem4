#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har
from Algorytmy import LeapFrog as LF
from Uklad import Uklad
from Kulka import Kulka
import numpy as np
import matplotlib.pyplot as plt

class Symulacje():
    def __init__(self, uklad, potencjal, algorytm, steps = 1000):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__steps = steps
        
    def run(self):
        lista_kul = self.__uklad.kulka_get
        for i in range(self.__steps):
            f = self.__potencjal.calc_forces(lista_kul)
            self.__algorytm.ruch(f, lista_kul)
        # testtuje
        return True
    
if __name__ == "__main__":
    kulka1 = Kulka(np.array([0]), 1, np.array([0]))
    kulka2 = Kulka(np.array([1]), 1, np.array([0]))
    kulki = [kulka1, kulka2]
    uklad = Uklad(kulki)
    potencjal = Har(k=10, x0=2)
    algorytm = LF()
    s = Symulacje(uklad, potencjal, algorytm)
    s.run()
    a1 = uklad.kulka_get[0].pos_get_all
    a2 = uklad.kulka_get[1].pos_get_all
    a3 = []
    for i in range(len(a1)):
        a3.append(abs(a1[i][0]-a2[i][0]))
    print(a1, a2)
    plt.plot(a1)
    plt.plot(a2)
    plt.show()
    plt.plot(a3)
    plt.show()