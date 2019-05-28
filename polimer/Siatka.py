#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Mer import Mer

class Siatak():
    def __init__(self, n = 10, E = 0):
        self.n = n
        self.__E = E
        self.__siatka = []
        for i in range(n):
            pom = []
            for j in range(n):
                pom.append(None)
            self.__siatka.append(pom)
        
    @property
    def siatka_get(self):
        siatka = []
        for i in self.__siatka:
            siatka.append(i[:])
        return siatka
    
    def siatka_set(self, new_siatka):
        self.__siatka = new_siatka
    
    @property
    def energy_get(self):
        energy = self.__E
        return energy
    
    def energy_set(self, new_energy):
        self.__E = new_energy
if __name__ == "__main__":
    s = Siatak(n = 25)
    temp = s.siatka_get
    m = Mer([12, 12])
    temp[m.pos_get[0]][m.pos_get[1]] = m
    s.siatka_set(temp)
    print(s.siatka_get)