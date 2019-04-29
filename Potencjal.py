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
    
    def calc_energy(self, uklad):
        e = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-2].pos_get_all[0][0] / ((len(uklad.kulka_get)/2)**(1/2) - 1)
        for i in uklad.imp_get['Har']:
            k1, k2 = i[0], i[1]
            lista_x = []
            x = k1.pos_get-k2.pos_get
            
            # tworzenie listy wektorow odleglosci
            lista_x.append(x)
            lista_x.append(k1.pos_get-(k2.pos_get + np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_x.append(k1.pos_get-(k2.pos_get - np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_x.append(k1.pos_get-(k2.pos_get + np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_x.append(k1.pos_get-(k2.pos_get - np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            
            # liczenie najmniejszej odleglosci
            lista_d = []
            for i in range(len(lista_x)):
                lista_d.append(np.linalg.norm(lista_x[i]))

            d = min(lista_d)
            ind = lista_d.index(d)
            x = lista_x[ind]
            v = x/d

            e[k1.id_get] += (self.__k/2)*((d - self.__x0)**2)*v
            e[k2.id_get] += (self.__k/2)*((d - self.__x0)**2)*v
        return e
    
    def calc_forces(self, uklad):
        f = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-2].pos_get_all[0][0] / ((len(uklad.kulka_get)/2)**(1/2) - 1)
        for i in uklad.imp_get['Har']:
            k1, k2 = i[0], i[1]
            lista_x = []
            x = k1.pos_get-k2.pos_get
            
            # tworzenie listy wektorow odleglosci
            lista_x.append(x)
            lista_x.append(k1.pos_get-(k2.pos_get + np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_x.append(k1.pos_get-(k2.pos_get - np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_x.append(k1.pos_get-(k2.pos_get + np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_x.append(k1.pos_get-(k2.pos_get - np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            
            # liczenie najmniejszej odleglosci
            lista_d = []
            for i in range(len(lista_x)):
                lista_d.append(np.linalg.norm(lista_x[i]))

            d = min(lista_d)
            ind = lista_d.index(d)
            x = lista_x[ind]
            v = x/d

            f[k1.id_get] += -self.__k*(d - self.__x0)*v
            f[k2.id_get] += self.__k*(d - self.__x0)*v
        return f
    
class Langevin(Potencjal):
    def __init__(self, tarcie = 1):
        self.__tarcie = tarcie
        
    def calc_energy(self, uklad):
        return np.zeros((len(uklad.kulka_get), uklad.dim_get))
    
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
        
    def calc_energy(self, uklad):
        e = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-2].pos_get_all[0][0] / ((len(uklad.kulka_get)/2)**(1/2) - 1)
        for i in uklad.imp_get['Lj']:
            k1, k2 = i[0], i[1]
            lista_r = []
            r = k1.pos_get-k2.pos_get
            lista_r.append(r)
            lista_r.append(k1.pos_get-(k2.pos_get + np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_r.append(k1.pos_get-(k2.pos_get - np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_r.append(k1.pos_get-(k2.pos_get + np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_r.append(k1.pos_get-(k2.pos_get - np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_d = []
            for i in range(len(lista_r)):
                lista_d.append(np.linalg.norm(lista_r[i]))

            d = min(lista_d)
            ind = lista_d.index(d)
            r = lista_r[ind]
            v = r/d
            e[k1.id_get] += 4*self.__eps*((self.__r0/d)**6 - (self.__r0/d)**12)*v
            e[k2.id_get] += 4*self.__eps*((self.__r0/d)**6 - (self.__r0/d)**12)*v
        return e
        
    def calc_forces(self, uklad):
        f = np.zeros((len(uklad.kulka_get), uklad.dim_get))
        odl_pom = uklad.kulka_get[-2].pos_get_all[0][0] / ((len(uklad.kulka_get)/2)**(1/2) - 1)
        for i in uklad.imp_get['Lj']:
            k1, k2 = i[0], i[1]
            lista_r = []
            r = k1.pos_get-k2.pos_get
            lista_r.append(r)
            lista_r.append(k1.pos_get-(k2.pos_get + np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_r.append(k1.pos_get-(k2.pos_get - np.array([0, uklad.kulka_get[-2].pos_get_all[0][1] + odl_pom])))
            lista_r.append(k1.pos_get-(k2.pos_get + np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_r.append(k1.pos_get-(k2.pos_get - np.array([uklad.kulka_get[-2].pos_get_all[0][0] + odl_pom, 0])))
            lista_d = []
            for i in range(len(lista_r)):
                lista_d.append(np.linalg.norm(lista_r[i]))

            d = min(lista_d)
            ind = lista_d.index(d)
            r = lista_r[ind]
            v = r/d
            f[k1.id_get] += 4*self.__eps*(12*(self.__r0/d)**12 - 6*(self.__r0/d)**6)*v
            f[k2.id_get] += -4*self.__eps*(12*(self.__r0/d)**12 - 6*(self.__r0/d)**6)*v
        return f