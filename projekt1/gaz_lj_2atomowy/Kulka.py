#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Kulka():
    def __init__(self, pol, m, v, idk):
        self.__polozenie = [pol]
        self.__masa = m
        self.__v = [v]
        self.__idk = idk
    
    # pobieranie ostatniej pozycji
    @property
    def pos_get(self):
        pozycja = self.__polozenie[-1]
        return pozycja
    
    # dodawanie nowej pozycji
    def pos_set(self, new_pos):
        self.__polozenie.append(new_pos)
    
    # pobieranie wszystkich pozycji
    @property
    def pos_get_all(self):
        pozycja = self.__polozenie
        return pozycja
    
    # pobieranie ostatniej predkosci
    @property
    def ver_get(self):
        ver = self.__v[-1]
        return ver
    
    # dodawanei nowej predkosci
    def ver_set(self, new_ver):
        self.__v.append(new_ver)
    
    # pobieranie id obiektu
    @property
    def id_get(self):
        idk = self.__idk
        return idk
    
    @property
    def m_get(self):
        ma = self.__masa
        return ma

if __name__ == "__main__":
    kulka = Kulka(np.array([1]), 7, np.array([1]))
    x = kulka.pos_get
    print(x)
    kulka.pos_set([2])
    x = kulka.pos_get
    print(x)
