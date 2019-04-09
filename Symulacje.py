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
#            print(f)
            self.__algorytm.ruch(f, self.__uklad.kulka_get)
        # testtuje
        return True
    
if __name__ == "__main__":
    kule = []
    n = 10
    for i in range(n):
        kule.append(Kulka(np.array([i]), 1, np.array([0]), idk = i))
#    kule.append(Kulka(np.array([n]), 1, np.array([0]), idk = n))
#    kulka5 = Kulka(np.array([3.1]), 1, np.array([0]), idk = 4)
    im = []
    for i in range(len(kule)-1):
        im.append([kule[i],kule[i+1]])
    
    uklad = Uklad(kule, dim =1, T = 300, imp = im)
    potencjal = [Har(k=1, x0=2), Lv(tarcie=0.9)]
    algorytm = LF()
    s = Symulacje(uklad, potencjal, algorytm, steps = 5000)
    s.run()
    
    pozycje = []
    for i in range(len(kule)):
        pozycje.append(uklad.kulka_get[i].pos_get_all)
    
#    odleglosci = []
#    for i in range(len(im)):
#        for j in range(len(a1)):
#            odleglosci.append(a1[i][0]-a2[i][0])
#    a1 = uklad.kulka_get[0].pos_get_all
#    a2 = uklad.kulka_get[1].pos_get_all
#    a3 = []
#    for i in range(len(a1)):
#        a3.append(a1[i][0]-a2[i][0])
#    print(a1, a2)
    for i in range(len(pozycje)):
        plt.plot(pozycje[i])
    plt.show()
#    plt.plot(a3)
#    plt.show()