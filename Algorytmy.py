#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as ran
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
    def __init__(self, t=100, dt=0.001):
        self.__atom = [0]
        self.__predkosc = [0]
        self.__lista_polozen = [self.__atom]
        self.__lista_predkosci = [self.__predkosc]
        self.__tarcie = 0.9
        self.__t = t
        self.__dt = dt
        self.__x = []
#        self.__y = []
#        self.__z = []
            
    def ruch(self, kulka):
        for i in range(self.__t):
#            self.__x.append(ran.uniform(-1,1))
#            self.__y.append(ran.uniform(-1,1))
#            self.__z.append(ran.uniform(-1,1))
#            norm = (math.sqrt((self.__x[i]**2)+(self.__y[i]**2)+(self.__z[i]**2)))
            f=ran.uniform(-1,1)/m
            pomocnicza_lista_pose = [0]
            pomocnicza_lista_ver = [0]
#            petla wykonywana j=dim
            for j in range(len(self.__atom)):
                pomocnicza_lista_ver[j] = kulka.v[-1] + f*self.__dt
                pomocnicza_lista_pose[j] = kulka.pose[-1] + pomocnicza_lista_ver[j]*self.__dt
        return pomocnicza_lista_pose, pomocnicza_lista_ver
            
            
        
    def update_pose(self):
        kulka.pose.append(ruch[0])
    
    def update_ver(self):
        kulka.v.append(ruch[1])