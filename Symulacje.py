#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har
from Algorytmy import LeapFrog as LP
from Uklad import Uklad
from Kulka import Kulka
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
            f = self.__potencjal.calc_forces(lista_kul[0], lista_kul[1])
            print('f ',f)
            for j in range(len(lista_kul)):
                algo = self.__algorytm.ruch(((-1)**j)*f, lista_kul[j])
                self.__algorytm.update_pos(algo[0], lista_kul[j])
                self.__algorytm.update_ver(algo[1], lista_kul[j])
        # testtuje
        return 'nowa pozycja'
    
if __name__ == "__main__":
    kulka1 = Kulka([0], 1, [0])
    kulka2 = Kulka([0], 1, [0])
    kulki = [kulka1, kulka2]
    uklad = Uklad(kulki)
    potencjal = Har()
    algorytm = LP()
    s = Symulacje(uklad, potencjal, algorytm)
    s.run()
    a1 = uklad.kulka_get[0].pos_get_all
    a2 = uklad.kulka_get[1].pos_get_all
    a3 = []
    for i in range(len(a1)):
        a3.append(a1[i][0]-a2[i][0])
#    print(a1, a2)
#    plt.plot(a1)
#    plt.plot(a2)
    plt.plot(a3)
    plt.show()