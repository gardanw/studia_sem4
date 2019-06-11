#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


class Mer():
    def __init__(self, pos, id, neighbor = [None, None]):
        self.__pos = pos
        self.__neighbor = neighbor
        self.__id = id
        self.__spin = np.random.choice([-1, 1])
        
    @property
    def pos_get(self):
        pos = self.__pos
        return pos
    
    def pos_set(self, new_pos):
        self.__pos = new_pos
        
    @property
    def spin_get(self):
        spin = self.__spin
        return spin
    
    def spin_set(self, new_spin):
        self.__spin = new_spin
        
    @property
    def nei_get(self):
        nei = self.__neighbor
        return nei
    
    def nei_set(self, new_nei):
        self.__neighbor = new_nei
        
    @property
    def id_get(self):
        id = self.__id
        return id
        
    def id_set(self, new_id):
        self.__id = new_id
        
if __name__ == "__main__":
    mer1 = Mer([12,12])
    print(mer1.nei_get)
    print(mer1.pos_get)
    mer1.pos_set([11,11])
    print(mer1.pos_get)
    mer2 = Mer([11,12])
    print(mer2.nei_get)
    print(mer2.pos_get)
    
    