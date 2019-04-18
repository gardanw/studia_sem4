#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har, Langevin as Lv
#from Potencjal import Langevin as Lv
from Algorytmy import LeapFrog as LF
from Uklad import Uklad
from Kulka import Kulka
from DrawSym import DrawSym as ds
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
#            print(f)
            self.__algorytm.ruch(f, self.__uklad.kulka_get)
        # testtuje
        return True
    
if __name__ == "__main__":
    kulki = []
    kulki.append(Kulka(np.array([0,0]), 1, np.array([0,0]), 0))
    kulki.append(Kulka(np.array([10,0]), 1, np.array([0,0]), 1))
    kulki.append(Kulka(np.array([20,0]), 1, np.array([0,0]), 2))
    kulki.append(Kulka(np.array([30,0]), 1, np.array([0,0]), 3))
    uklad = Uklad(kulki, dim = len(kulki[0].pos_get), T = 300, imp = [[kulki[0], kulki[1]], [kulki[1], kulki[2]], [kulki[2], kulki[3]], [kulki[3], kulki[0]]])
    pot = [Har(k = 0.1, x0 = 2), Lv(tarcie = 0.9)]
    alg = LF()
    sym = Symulacje(uklad, pot, alg, steps=10000)
    sym.run()
#    print('kulka 0: \n', kulki[0].pos_get_all, '\n kulka 1: \n', kulki[1].pos_get_all)
    print(kulki[0].pos_get_all[30][0])
    plt.plot(kulki[0].pos_get_all)
    plt.plot(kulki[1].pos_get_all)
    plt.plot(kulki[2].pos_get_all)
    plt.plot(kulki[3].pos_get_all)
    plt.show()
    ds([kulki[0].pos_get_all,kulki[1].pos_get_all,kulki[2].pos_get_all,kulki[3].pos_get_all])