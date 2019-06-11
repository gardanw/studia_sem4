#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Mer import Mer
from Siatka import Siatak
from Move import Move
import random as ran
import numpy as np
import matplotlib.pyplot as plt
import copy
import imageio

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
        
        steps = 100
        temp_range = np.linspace(1, 2000, 30)
        energy = np.zeros(len(temp_range))
        std = np.zeros(len(temp_range))
        iterator = 0
        for T in temp_range:
            self.__siatka.T_set(T)
            image = []
            pom_polimer = copy.deepcopy(self.__polimer)
            pom_siatka = copy.deepcopy(self.__siatka)
            energi_all = []
            for step in range(steps):
                for i in pom_polimer:
                    if i.pos_get[0] == 0.:
                        for j in pom_polimer:
                            j.pos_set([j.pos_get[0] + (len(pom_siatka.siatka_get) // 2) - 2, j.pos_get[1]])
                    if i.pos_get[1] == 0.:
                        for j in pom_polimer:
                            j.pos_set([j.pos_get[0], j.pos_get[1] + (len(pom_siatka.siatka_get) // 2) - 2] )
                    if i.pos_get[0] == float(len(pom_siatka.siatka_get) - 1):
                        for j in pom_polimer:
                            j.pos_set([j.pos_get[0] - (len(pom_siatka.siatka_get) // 2) + 2, j.pos_get[1]])
                    if i.pos_get[0] == float(len(pom_siatka.siatka_get) - 1):
                        for j in pom_polimer:
                            j.pos_set([j.pos_get[0], j.pos_get[1] - (len(pom_siatka.siatka_get) // 2) + 2])
                print(step, T)
                temp = pom_siatka.siatka_get
                temp_polimer = copy.deepcopy(pom_polimer)
                los_mer = np.random.choice(temp_polimer)
                
                if None in los_mer.nei_get:
                    x = [0,1]
                    los_x = np.random.choice(x)
                    if los_x == 0:
                        self.__ruchy.ogon(los_mer, temp)
                    elif los_x == 1:
                        self.__ruchy.reptacja(los_mer, temp, temp_polimer)
                elif None not in los_mer.nei_get:
                    flaga = False
                    flaga = self.__ruchy.rog(los_mer, temp)
                    if flaga == False:
                        self.__ruchy.petla(los_mer, temp)
                matrix = matrix_nei(temp_polimer)
    #            for i in matrix:
    #                print(i)
                energia = 0
                for i in matrix:
                    energia += sum(i)
                energia -= 2*(len(matrix)-1)
                
                if energia <= pom_siatka.energy_get:
                    pom_siatka.siatka_set(temp)
                    pom_siatka.energy_set(energia)
                    pom_polimer = temp_polimer
                    matrix = matrix_nei(pom_polimer)
                    energi_all.append(energia)
    #                for i in matrix:
    #                    print(i)
#                    print("zamiana")
                    
                elif energia > pom_siatka.energy_get:
                    prawdo = ran.random()
                    if prawdo > np.exp(-(energia - pom_siatka.energy_get)/pom_siatka.T_get):
                        pom_siatka.siatka_set(temp)
                        pom_siatka.energy_set(energia)
                        pom_polimer = temp_polimer
                        matrix = matrix_nei(pom_polimer)
                        energi_all.append(energia)
    #                    for i in matrix:
    #                        print(i)
#                        print("zamiana")
                
                uklad = np.zeros([len(pom_siatka.siatka_get),len(pom_siatka.siatka_get)])
                for i in pom_polimer:
                    uklad[i.pos_get[0]][i.pos_get[1]] = i.id_get
    #            for i in uklad:
    #                print(i)
                p=[]
                q=[]
                for i in range(len(pom_polimer)):
    #                print(pom_polimer[i].pos_get)
                    p.append(pom_polimer[i].pos_get[0])
                    q.append(pom_polimer[i].pos_get[1])
                fig, ax = plt.subplots()
                plt.plot(p,q, 'ro-')
                plt.axis([0,30,0,30])
                fig.canvas.draw()
                image.append(np.array(fig.canvas.renderer._renderer))
                plt.close('all')
            energy[iterator] = np.mean(energi_all)
            std[iterator] = np.std(energi_all)
            imageio.mimsave("temperatura{0}.gif".format(T), image)
            iterator += 1
        plt.plot(energy)
        plt.plot(std)
        plt.savefig('wyktes.png')

            
            
if __name__ == "__main__":
    s = Siatak(n = 30)
    temp = s.siatka_get
    polimer = []
    m0 = Mer(np.array([int(s.n/2), int(s.n/2)]), id = 1)
    temp[m0.pos_get[0]][m0.pos_get[1]] = m0
    polimer.append(m0)
#    print(temp == s.siatka_get)
    
    for i in range(14):
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
#    for i in matrix:
#        print(i)
#    print(matrix)
    
    energy = 0
    for i in matrix:
        energy += sum(i)
    energy -= 2*(len(matrix)-1)
    
    s.energy_set(energy)
    
    uklad = np.zeros([len(s.siatka_get),len(s.siatka_get)])
    for i in polimer:
        uklad[i.pos_get[0]][i.pos_get[1]] = i.id_get
#    for i in uklad:
#        print(i)
        
    symulacja.sym()