#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Kulka import Kulka
import numpy as np
class Uklad():
    def __init__(self, lista_kulek, dim, T, imp):
        self.__lista_kulek = lista_kulek
        self.__dim = dim
        self.__T = T
        self.__imp = imp
    
    def __iter__(self):
        yield from self.__lista_kulek
        
    @property    
    def kulka_get(self):
        kul = self.__lista_kulek
        return kul
    
    @property    
    def dim_get(self):
        dime = self.__dim
        return dime
    
    @property    
    def T_get(self):
        tem = self.__T
        return tem
    
    @property    
    def imp_get(self):
        im = self.__imp
        return im

if __name__ == "__main__":
    kulka1 = Kulka(np.array([1]), 1, np.array([0]))
    kulka2 = Kulka(np.array([0]), 1, np.array([0]))
    lista = [kulka1,kulka2]
    uklad = Uklad(lista)
    k1 = uklad.kulka_get
    k2 = k1[0]
    print(k2)