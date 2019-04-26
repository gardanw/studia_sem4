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
        f = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-1].pos_get_all[0][0] / (len(uklad.kulka_get)**(1/2) - 1)
#        print('pom', odl_pom, uklad.kulka_get[-1].pos_get_all[0][0],(len(uklad.kulka_get)**(1/2) - 1) )
        for i in uklad.imp_get:
            k1, k2 = i[0], i[1]
            lista_x = []
            x = k1.pos_get-k2.pos_get
            
            # tworzenie listy wektorow odleglosci
            lista_x.append(x)
            lista_x.append(x + np.array([0, uklad.kulka_get[-1].pos_get_all[0][1] + odl_pom]))
            lista_x.append(x - np.array([0, uklad.kulka_get[-1].pos_get_all[0][1] - odl_pom]))
            lista_x.append(x + np.array([uklad.kulka_get[-1].pos_get_all[0][0] + odl_pom, 0]))
            lista_x.append(x - np.array([uklad.kulka_get[-1].pos_get_all[0][0] - odl_pom, 0]))
            
            # liczenie najmniejszej odleglosci
            lista_d = []
            for i in range(len(lista_x)):
                if np.linalg.norm(lista_x[i]) != 0.0:
                    lista_d.append(np.linalg.norm(lista_x[i]))
                else:
                    lista_d.append(np.linalg.norm(lista_x[i])+0.01)
            d = min(lista_d)
            
#            print(k1.id_get,k2.id_get,'\n', lista_x,lista_d, d)
            v = x/d
#            f1 = -self.__k*(d - self.__x0)*v
#            print(f1)
            f[k1.id_get] += -self.__k*(d - self.__x0)*v
            f[k2.id_get] += self.__k*(d - self.__x0)*v
#            print(self.__k,'*(',d,' - ',self.__x0,')*',v,'\n', f[k1.id_get])
            
        return f
    
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

class LennardJones(Potencjal):
    def __init__(self, r0, eps = 1):
        self.__r0 = r0
        self.__eps = eps
        
    def calc_forces(self, uklad):
        f = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-1].pos_get_all[0][0] / (len(uklad.kulka_get)**(1/2) - 1)
#        print('pom', odl_pom, uklad.kulka_get[-1].pos_get_all[0][0],(len(uklad.kulka_get)**(1/2) - 1) )
        for i in uklad.imp_get:
            k1, k2 = i[0], i[1]
            lista_r = []
            r = k1.pos_get-k2.pos_get
            lista_r.append(r)
            lista_r.append(r + np.array([0, uklad.kulka_get[-1].pos_get_all[0][1] + odl_pom]))
            lista_r.append(r - np.array([0, uklad.kulka_get[-1].pos_get_all[0][1] - odl_pom]))
            lista_r.append(r + np.array([uklad.kulka_get[-1].pos_get_all[0][0] + odl_pom, 0]))
            lista_r.append(r - np.array([uklad.kulka_get[-1].pos_get_all[0][0] - odl_pom, 0]))
            lista_d = []
            for i in range(len(lista_r)):
                lista_d.append(np.linalg.norm(lista_r[i]))
                if np.linalg.norm(lista_r[i]) != 0.0:
                    lista_d.append(np.linalg.norm(lista_r[i]))
                else:
                    lista_d.append(np.linalg.norm(lista_r[i])+0.00001)
            d = min(lista_d)
#            d = np.linalg.norm(r)
#            print(k1.id_get,k2.id_get,'\n', lista_r,lista_d, d)
            v = r/d
            f[k1.id_get] += self.__eps*((self.__r0/d)**12 - 2*(self.__r0/d)**6)*v
            f[k2.id_get] += -self.__eps*((self.__r0/d)**12 - 2*(self.__r0/d)**6)*v
#            print(self.__eps, '*((', self.__r0, '/', d, ')**', 12, '-', 2, '*', '(', self.__r0, '/', d, ')**', 6, ')*', v, '\n', f[k1.id_get])
        return f