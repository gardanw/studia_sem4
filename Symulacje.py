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
    n = 3
    id = 0
    for i in range(n):
        for j in range(n):
            kulki.append(Kulka(np.array([i*100, j*100]), 1, np.array([0,0]), idk = id))
            id += 1
    print(id)
#    kulki.append(Kulka(np.array([100,100]), 1, np.array([0,0]), 0))
#    kulki.append(Kulka(np.array([100,200]), 1, np.array([0,0]), 1))
#    kulki.append(Kulka(np.array([200,100]), 1, np.array([0,0]), 2))
#    kulki.append(Kulka(np.array([200,200]), 1, np.array([0,0]), 3))
    im = []
    for i in kulki:
        for j in kulki:
            if i != j:
                im.append([i,j])
                
#    imp = [[kulki[0], kulki[1]], [kulki[1], kulki[2]], [kulki[2], kulki[3]], [kulki[3], kulki[0]]]
    uklad = Uklad(kulki, dim = len(kulki[0].pos_get), T = 300, imp = im)
    pot = [Har(k = 0.1, x0 = 2)]
    alg = LF()
    sym = Symulacje(uklad, pot, alg, steps=5000)
    sym.run()
#    print('kulka 0: \n', kulki[0].pos_get_all, '\n kulka 1: \n', kulki[1].pos_get_all)
    print(kulki[0].pos_get_all[30][0])
    plt.plot(kulki[0].pos_get_all)
    plt.plot(kulki[1].pos_get_all)
    plt.plot(kulki[2].pos_get_all)
    plt.plot(kulki[3].pos_get_all)
    plt.show()
    lista_pos = []
    for i in range(len(kulki)):
        lista_pos.append(kulki[i].pos_get_all)
    ds(lista_pos)