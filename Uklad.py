#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Kulka import Kulka
import numpy as np
class Uklad():
    def __init__(self, lista_kulek):
        self.__lista_kulek = lista_kulek
        self.__powiazania = {}
        for i in range(len(self.__lista_kulek)):
            lista_oddzialujacych =[]
            for j in range(len(self.__lista_kulek)):
                if i != j:
                    lista_oddzialujacych.append(self.__lista_kulek[j]) 
            self.__powiazania[self.__lista_kulek[i]] = lista_oddzialujacych
        
    @property    
    def kulka_get(self):
        kul = self.__lista_kulek
        return kul

if __name__ == "__main__":
    kulka1 = Kulka(np.array([1]), 1, np.array([0]))
    kulka2 = Kulka(np.array([0]), 1, np.array([0]))
    lista = [kulka1,kulka2]
    uklad = Uklad(lista)
    k1 = uklad.kulka_get
    k2 = k1[0]
    print(k2)