#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Uklad import Uklad
from Kulka import Kulka
import numpy as np

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
    
    def calc_forces(self, kulki):
        k1, k2 = kulki[0], kulki[1]
        x = k1.pos_get-k2.pos_get
        d = np.linalg.norm(x)
        v = x / d
        f1 = -self.__k*(d - self.__x0)*v
        f2 = self.__k*(d - self.__x0)*v
        return [f1,f2]
    
#if __name__ == "__main__":
