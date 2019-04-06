#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.constants import Boltzmann as K
from scipy.constants import Avogadro as Na
import numpy as np
import random as ran

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
    
    def calc_forces(self, uklad):
        k1, k2 = uklad.kulka_get[0], uklad.kulka_get[1]
        x = k1.pos_get-k2.pos_get
        d = np.linalg.norm(x)
        v = x / d
        f1 = -self.__k*(d - self.__x0)*v
        f2 = self.__k*(d - self.__x0)*v
        return [f1,f2]
    
class Langevin(Potencjal):
    def __init__(self, tarcie = 1):
        self.__tarcie = tarcie
    
    def calc_forces(self, uklad):
        kb = K*Na
        f = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        for i in range(len(uklad.kulka_get)):
            for j in range(uklad.dim_get):
                f[i][j] = np.sqrt(2*self.__tarcie*kb*uklad.T_get)*ran.gauss(0, 1)
        return f
