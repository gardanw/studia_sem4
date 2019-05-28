#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Mer import Mer
from Siatka import Siatak
from Move import Move
import random as ran
import numpy as np

def matrix_nei(polimer):
    matrix = []
    for i in range(len(polimer)):
        pom = []
        for j in range(len(polimer)):
            pom.append(0)
        matrix.append(pom)
    for i in range(len(polimer)):
        for j in range(len(polimer)):
            if i !=  j:
                if ((polimer[i].pos_get[0] == polimer[j].pos_get[0] and polimer[i].pos_get[1] == polimer[j].pos_get[1]-1)
                    or (polimer[i].pos_get[0] == polimer[j].pos_get[0] and polimer[i].pos_get[1] == polimer[j].pos_get[1]+1) \
                    or (polimer[i].pos_get[0] == polimer[j].pos_get[0]-1 and polimer[i].pos_get[1] == polimer[j].pos_get[1])
                    or (polimer[i].pos_get[0] == polimer[j].pos_get[0]+1 and polimer[i].pos_get[1] == polimer[j].pos_get[1])):
                    matrix[i][j] = 1
    return matrix

class Symulacja():
    def __init__(self, siatka, polimer, ruchy = Move()):
        self.__siatka = siatka
        self.__polimer = polimer
        self.__ruchy = ruchy
    
    def sym(self):
        temp = self.__siatka.siatka_get
        los_mer = np.random.choice(self.__polimer)
        
        if None in los_mer.nei_get:
            x = [0,1]
            los_x = np.random.choice(x)
            if los_x == 0:
                self.__ruchy.ogon(los_mer, temp)
            elif los_x == 1:
                self.__ruchy.reptacja(los_mer, temp, self.__polimer)
        elif None not in los_mer.nei_get:
            flaga = False
            flaga = self.__ruchy.rog(los_mer, temp)
            if flaga == False:
                self.__ruchy.petla(los_mer, temp)
        matrix = matrix_nei(polimer)
        for i in matrix:
            print(i)
        uklad = []
        for i in range(len(temp)):
            pom = []
            for j in range(len(temp[i])):
                if temp[i][j] == None:
                    pom.append(0)
                else:
                    pom.append(temp[i][j].id_get)
            uklad.append(pom)
        for i in uklad:
            print(i)
            
            
if __name__ == "__main__":
    s = Siatak(n = 10)
    temp = s.siatka_get
    polimer = []
    m0 = Mer(np.array([int(s.n/2), int(s.n/2)]), id = 1)
    temp[m0.pos_get[0]][m0.pos_get[1]] = m0
    polimer.append(m0)
    print(temp == s.siatka_get)
    
    for i in range(4):
        los = []
        if temp[polimer[-1].pos_get[0] - 1][polimer[-1].pos_get[1]] == None:
            los.append(0)
        if temp[polimer[-1].pos_get[0] + 1][polimer[-1].pos_get[1]] == None:
            los.append(1)
        if temp[polimer[-1].pos_get[0]][polimer[-1].pos_get[1] - 1] == None:
            los.append(2)
        if temp[polimer[-1].pos_get[0]][polimer[-1].pos_get[1] + 1] == None:
            los.append(3)
        
        los_pos = np.random.choice(los)
        if los_pos == 0:
            polimer.append(Mer(np.array([polimer[-1].pos_get[0] - 1,polimer[-1].pos_get[1]]), id = i+2))
        elif los_pos == 1:
            polimer.append(Mer(np.array([polimer[-1].pos_get[0] + 1,polimer[-1].pos_get[1]]), id = i+2))
        elif los_pos == 2:
            polimer.append(Mer(np.array([polimer[-1].pos_get[0],polimer[-1].pos_get[1] - 1]), id = i+2))
        elif los_pos == 3:
            polimer.append(Mer(np.array([polimer[-1].pos_get[0],polimer[-1].pos_get[1] + 1]), id = i+2))
        temp[polimer[-1].pos_get[0]][polimer[-1].pos_get[1]] = polimer[-1]
    
    s.siatka_set(temp)
    symulacja = Symulacja(s, polimer)
    # tworzenie lancucha glownego
    for i in range(len(polimer)):
        if  i == 0:
            polimer[i].nei_set([None,polimer[i+1]])
        elif i != 0 and i != len(polimer) - 1:
            polimer[i].nei_set([polimer[i-1],polimer[i+1]])
        elif i == len(polimer) -1:
            polimer[i].nei_set([polimer[i-1],None])
     
    matrix = matrix_nei(polimer)
    for i in matrix:
        print(i)
#    print(matrix)
    
    energy = 0
    for i in matrix:
        energy += sum(i)
    energy -= 2*(len(matrix)-1)
    
    s.energy_set(energy)
    
    uklad = []
    for i in range(len(s.siatka_get)):
        pom = []
        for j in range(len(s.siatka_get[i])):
            if s.siatka_get[i][j] == None:
                pom.append(0)
            else:
                pom.append(s.siatka_get[i][j].id_get)
        uklad.append(pom)
    for i in uklad:
        print(i)
        
    symulacja.sym()