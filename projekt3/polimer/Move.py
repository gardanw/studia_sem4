#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Move():        
    def ogon(self, los_mer, temp):
        pomo = los_mer.nei_get.index(None)
        if pomo == 0:
            mer_pom = los_mer.nei_get[1]
        elif pomo == 1:
            mer_pom = los_mer.nei_get[0]
        los = []
        if temp[mer_pom.pos_get[0] - 1][mer_pom.pos_get[1]] == None:
            los.append(0)
        if temp[mer_pom.pos_get[0] + 1][mer_pom.pos_get[1]] == None:
            los.append(1)
        if temp[mer_pom.pos_get[0]][mer_pom.pos_get[1] - 1] == None:
            los.append(2)
        if temp[mer_pom.pos_get[0]][mer_pom.pos_get[1] + 1] == None:
            los.append(3)
            
        if len(los) == 0:
            text = 'nie mozna wykonac ruchu'
            return text
        los_pos = np.random.choice(los)
        temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
#        pom_pos = los_mer.pos_get
        if los_pos == 0:
            los_mer.pos_set(np.array([mer_pom.pos_get[0] - 1, mer_pom.pos_get[1]]))
        elif los_pos == 1:
            los_mer.pos_set(np.array([mer_pom.pos_get[0] + 1, mer_pom.pos_get[1]]))
        elif los_pos == 2:
            los_mer.pos_set(np.array([mer_pom.pos_get[0], mer_pom.pos_get[1] - 1]))
        elif los_pos == 3:
            los_mer.pos_set(np.array([mer_pom.pos_get[0], mer_pom.pos_get[1] + 1]))
        temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = los_mer
#        temp[pom_pos[0]][pom_pos[1]] = None
#        print('ogon')
        
    def reptacja(self, los_mer, temp, polimer):
        if los_mer.nei_get[0] == None:
            mer_pom = polimer[-1]
            pom = polimer.pop(0)
            polimer.append(pom)
            polimer[0].nei_set([None, polimer[1]])
            polimer[1].nei_set([polimer[0],polimer[2]])
            polimer[-2].nei_set([polimer[-3], polimer[-1]])
            polimer[-1].nei_set([polimer[-2], None])
        elif los_mer.nei_get[1] == None:
            mer_pom = polimer[0]
            pom = polimer.pop(-1)
            polimer.insert(0,pom)
            polimer[0].nei_set([None, polimer[1]])
            polimer[1].nei_set([polimer[0], polimer[2]])
            polimer[-2].nei_set([polimer[-3], polimer[-1]])
            polimer[-1].nei_set([polimer[-2], None])
        los = []
        if temp[mer_pom.pos_get[0] - 1][mer_pom.pos_get[1]] == None:
            los.append(0)
        if temp[mer_pom.pos_get[0] + 1][mer_pom.pos_get[1]] == None:
            los.append(1)
        if temp[mer_pom.pos_get[0]][mer_pom.pos_get[1] - 1] == None:
            los.append(2)
        if temp[mer_pom.pos_get[0]][mer_pom.pos_get[1] + 1] == None:
            los.append(3)
        
        if len(los) == 0:
            text = 'nie mozna wykonac ruchu'
            return text
        
        los_pos = np.random.choice(los)
        pom_pos = los_mer.pos_get
        if los_pos == 0:
            los_mer.pos_set(np.array([mer_pom.pos_get[0] - 1, mer_pom.pos_get[1]]))
        elif los_pos == 1:
            los_mer.pos_set(np.array([mer_pom.pos_get[0] + 1, mer_pom.pos_get[1]]))
        elif los_pos == 2:
            los_mer.pos_set(np.array([mer_pom.pos_get[0], mer_pom.pos_get[1] - 1]))
        elif los_pos == 3:
            los_mer.pos_set(np.array([mer_pom.pos_get[0], mer_pom.pos_get[1] + 1]))
        temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = los_mer
        temp[pom_pos[0]][pom_pos[1]] = None
        
        
#        print('reptacja')
        
    def rog(self, los_mer, temp):
        pom_pos = los_mer.pos_get
        if (los_mer.nei_get[0].pos_get[0] == los_mer.pos_get[0] + 1 and los_mer.nei_get[1].pos_get[1] == los_mer.pos_get[1] + 1
            or los_mer.nei_get[1].pos_get[0] == los_mer.pos_get[0] + 1 and los_mer.nei_get[0].pos_get[1] == los_mer.pos_get[1] + 1):
            if temp[los_mer.pos_get[0] + 1][los_mer.pos_get[1] + 1] == None:
                temp[los_mer.pos_get[0] + 1][los_mer.pos_get[1] + 1] = los_mer
                temp[pom_pos[0]][pom_pos[1]] = None
                los_mer.pos_set(np.array([los_mer.pos_get[0] + 1,los_mer.pos_get[1] + 1]))
#                print('rog')
                return True
        elif (los_mer.nei_get[0].pos_get[0] == los_mer.pos_get[0] - 1 and los_mer.nei_get[1].pos_get[1] == los_mer.pos_get[1] + 1
              or los_mer.nei_get[1].pos_get[0] == los_mer.pos_get[0] - 1 and los_mer.nei_get[0].pos_get[1] == los_mer.pos_get[1] + 1):
            if temp[los_mer.pos_get[0] - 1][los_mer.pos_get[1] + 1] == None:
                temp[los_mer.pos_get[0] - 1][los_mer.pos_get[1] + 1] = los_mer
                temp[pom_pos[0]][pom_pos[1]] = None
                los_mer.pos_set(np.array([los_mer.pos_get[0] - 1,los_mer.pos_get[1] + 1]))
#                print('rog')
                return True
        elif (los_mer.nei_get[0].pos_get[0] == los_mer.pos_get[0] + 1 and los_mer.nei_get[1].pos_get[1] == los_mer.pos_get[1] - 1
              or los_mer.nei_get[1].pos_get[0] == los_mer.pos_get[0] + 1 and los_mer.nei_get[0].pos_get[1] == los_mer.pos_get[1] - 1):
            if temp[los_mer.pos_get[0] + 1][los_mer.pos_get[1] - 1] == None:
                temp[los_mer.pos_get[0] + 1][los_mer.pos_get[1] - 1] = los_mer
                temp[pom_pos[0]][pom_pos[1]] = None
                los_mer.pos_set(np.array([los_mer.pos_get[0] + 1,los_mer.pos_get[1] - 1]))
#                print('rog')
                return True
        elif (los_mer.nei_get[0].pos_get[0] == los_mer.pos_get[0] - 1 and los_mer.nei_get[1].pos_get[1] == los_mer.pos_get[1] - 1
              or los_mer.nei_get[1].pos_get[0] == los_mer.pos_get[0] - 1 and los_mer.nei_get[0].pos_get[1] == los_mer.pos_get[1] - 1):
            if temp[los_mer.pos_get[0] - 1][los_mer.pos_get[1] - 1] == None:
                temp[los_mer.pos_get[0] - 1][los_mer.pos_get[1] - 1] = los_mer
                temp[pom_pos[0]][pom_pos[1]] = None
                los_mer.pos_set(np.array([los_mer.pos_get[0] - 1,los_mer.pos_get[1] - 1]))
#                print('rog')
                return True
            
    def petla(self, los_mer, temp):
        if (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0] + 1
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1]
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1] + 1
            and los_mer.nei_get[1].pos_get[0] == los_mer.nei_get[1].nei_get[1].pos_get[0] + 1
            and los_mer.nei_get[1].pos_get[1] == los_mer.nei_get[1].nei_get[1].pos_get[1]
            and temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]] == None
            and temp[los_mer.pos_get[0]+2][los_mer.pos_get[0]+1] == None):
            temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]] = los_mer
            temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]+1] = los_mer.nei_get[1]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]+1] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0]+2,los_mer.pos_get[1]]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]+1]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1] - 1
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0] + 1
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1]
            and los_mer.nei_get[0].pos_get[0] == los_mer.nei_get[0].nei_get[0].pos_get[0] + 1
            and los_mer.nei_get[0].pos_get[1] == los_mer.nei_get[0].nei_get[0].pos_get[1]
            and temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]] == None
            and temp[los_mer.pos_get[0]+2][los_mer.pos_get[0]-1] == None):
            temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]] = los_mer
            temp[los_mer.pos_get[0]+2][los_mer.pos_get[1]-1] = los_mer.nei_get[0]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]-1] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0]+2,los_mer.pos_get[1]]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]-1]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0] - 1
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1]
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1] - 1
            and los_mer.nei_get[1].pos_get[0] == los_mer.nei_get[1].nei_get[1].pos_get[0] - 1
            and los_mer.nei_get[1].pos_get[1] == los_mer.nei_get[1].nei_get[1].pos_get[1]
            and temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]] == None
            and temp[los_mer.pos_get[0]-2][los_mer.pos_get[0]+1] == None):
            temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]] = los_mer
            temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]+1] = los_mer.nei_get[1]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]+1] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0]-2,los_mer.pos_get[1]]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]+1]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1] - 1
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0] - 1
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1]
            and los_mer.nei_get[0].pos_get[0] == los_mer.nei_get[0].nei_get[0].pos_get[0] - 1
            and los_mer.nei_get[0].pos_get[1] == los_mer.nei_get[0].nei_get[0].pos_get[1]
            and temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]] == None
            and temp[los_mer.pos_get[0]-2][los_mer.pos_get[0]-1] == None):
            temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]] = los_mer
            temp[los_mer.pos_get[0]-2][los_mer.pos_get[1]-1] = los_mer.nei_get[0]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]-1] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0]-2,los_mer.pos_get[1]]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]-1]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1] + 1
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0] - 1
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1]
            and los_mer.nei_get[1].pos_get[0] == los_mer.nei_get[1].nei_get[1].pos_get[0]
            and los_mer.nei_get[1].pos_get[1] == los_mer.nei_get[1].nei_get[1].pos_get[1] +1
            and temp[los_mer.pos_get[0]][los_mer.pos_get[1]+2] == None
            and temp[los_mer.pos_get[0]-1][los_mer.pos_get[0]+2] == None):
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]+2] = los_mer
            temp[los_mer.pos_get[0]-1][los_mer.pos_get[1]+2] = los_mer.nei_get[1]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]-1][los_mer.pos_get[1]] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]+2]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0]-1,los_mer.pos_get[1]]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0] + 1
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1]
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1] + 1
            and los_mer.nei_get[0].pos_get[0] == los_mer.nei_get[0].nei_get[0].pos_get[0]
            and los_mer.nei_get[0].pos_get[1] == los_mer.nei_get[0].nei_get[0].pos_get[1] + 1
            and temp[los_mer.pos_get[0]][los_mer.pos_get[1]+2] == None
            and temp[los_mer.pos_get[0]+1][los_mer.pos_get[0]+2] == None):
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]+2] = los_mer
            temp[los_mer.pos_get[0]+1][los_mer.pos_get[1]+2] = los_mer.nei_get[0]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]+1][los_mer.pos_get[1]] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]+2]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0]+1,los_mer.pos_get[1]]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1] - 1
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0] + 1
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1]
            and los_mer.nei_get[1].pos_get[0] == los_mer.nei_get[1].nei_get[1].pos_get[0]
            and los_mer.nei_get[1].pos_get[1] == los_mer.nei_get[1].nei_get[1].pos_get[1] - 1
            and temp[los_mer.pos_get[0]][los_mer.pos_get[1]-2] == None
            and temp[los_mer.pos_get[0]-1][los_mer.pos_get[0]-2] == None):
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]-2] = los_mer
            temp[los_mer.pos_get[0]+1][los_mer.pos_get[1]-2] = los_mer.nei_get[1]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]+1][los_mer.pos_get[1]] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]-2]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0]+1,los_mer.pos_get[1]]))
#            print('petla')
        elif (los_mer.pos_get[0] == los_mer.nei_get[0].pos_get[0] - 1
            and los_mer.pos_get[1] == los_mer.nei_get[0].pos_get[1]
            and los_mer.pos_get[0] == los_mer.nei_get[1].pos_get[0]
            and los_mer.pos_get[1] == los_mer.nei_get[1].pos_get[1] - 1
            and los_mer.nei_get[0].pos_get[0] == los_mer.nei_get[0].nei_get[0].pos_get[0]
            and los_mer.nei_get[0].pos_get[1] == los_mer.nei_get[0].nei_get[0].pos_get[1] - 1
            and temp[los_mer.pos_get[0]][los_mer.pos_get[1]-2] == None
            and temp[los_mer.pos_get[0]-1][los_mer.pos_get[0]-2] == None):
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]-2] = los_mer
            temp[los_mer.pos_get[0]-1][los_mer.pos_get[1]-2] = los_mer.nei_get[0]
            temp[los_mer.pos_get[0]][los_mer.pos_get[1]] = None
            temp[los_mer.pos_get[0]-1][los_mer.pos_get[1]] = None
            los_mer.pos_set(np.array([los_mer.pos_get[0],los_mer.pos_get[1]-2]))
            los_mer.nei_get.pos_set(np.array([los_mer.pos_get[0]-1,los_mer.pos_get[1]]))
#            print('petla')