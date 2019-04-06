#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har
from Potencjal import Langevin as Lv
from Algorytmy import LeapFrog as LF
from Uklad import Uklad
from Kulka import Kulka
import numpy as np
import matplotlib.pyplot as plt

class Symulacje():
    def __init__(self, uklad, potencjal, algorytm, steps = 5000):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__steps = steps
        
    def run(self):
        for i in range(self.__steps):
            f = np.zeros((len(self.__uklad.kulka_get), self.__uklad.dim_get))
            for p in self.__potencjal:
                f += p.calc_forces(self.__uklad)
            self.__algorytm.ruch(f, self.__uklad.kulka_get)
        # testtuje
        return True
    
if __name__ == "__main__":
    kulka1 = Kulka(np.array([5]), 1, np.array([0]))
    kulka2 = Kulka(np.array([-2]), 1, np.array([0]))
#    kulka3 = Kulka(np.array([7]), 1, np.array([0]))
    kulki = [kulka1, kulka2]
#    imp = [[kulka1,kulka2], [kulka2,kulka3]]
    uklad = Uklad(kulki, dim =1, T = 300)
    potencjal = [Har(k=1, x0=2), Lv(tarcie = 0.9)]
    algorytm = LF()
    s = Symulacje(uklad, potencjal, algorytm, steps = 10000)
    s.run()
    a1 = uklad.kulka_get[0].pos_get_all
    a2 = uklad.kulka_get[1].pos_get_all
    a3 = []
    for i in range(len(a1)):
        a3.append(a1[i][0]-a2[i][0])
#    print(a1, a2)
    plt.plot(a1)
    plt.plot(a2)
    plt.show()
    plt.plot(a3)
    plt.show()