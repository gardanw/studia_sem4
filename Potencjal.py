#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Potencjal:
    def calc_energy():
        pass
    def calc_forces():
        pass
    
class Harmoniczny(Potencjal):
    def __init__(self, k=1, x0=0):
        self.__k = k
        self.__x0 = x0
    
    def calc_energy(self, k1, k2):
        x = abs(k1.poz[0] - k2.poz[0])
        return (self.__k/2)*(x - self.__x0)**2
    
    def calc_forces(self, k1, k2):
        x = abs(k1.poz[0] - k2.poz[0])
        return -1*self.k*(x-self.x0)