#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as ran
import numpy as np
import math
from Uklad import Uklad
from Kulka import Kulka

class Algorytmy:
    def update_pose(self):
        pass
    def update_ver(self):
        pass
    
class LeapFrog(Algorytmy):
    def __init__(self, dt=0.01):
        self.__dimension = 1
        self.__tarcie = 0.9
        self.__dt = dt
#        self.__x = []
    def update_pos(self, new_pos, kulka):
        kulka.pos_set(new_pos)
    
    def update_ver(self, new_ver, kulka):
        kulka.ver_set(new_ver)
    
    def ruch(self, force, kulka):
#        self.__x.append(ran.uniform(-1,1))
        f=force
        pomocnicza_lista_pos = [0]
        pomocnicza_lista_ver = [0]
#        petla wykonywana j=dim
        for j in range(self.__dimension):
            pomocnicza_lista_ver[j] = kulka.ver_get[j] + f*self.__dt
            pomocnicza_lista_pos[j] = kulka.pos_get[j] + pomocnicza_lista_ver[j]*self.__dt
        return pomocnicza_lista_pos, pomocnicza_lista_ver
            
            
        
