#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Kulka():
    def __init__(self, pol, m, v):
        self.__polozenie = [pol]
        self.__masa = m
        self.__v = [v]
    
    @property
    def pos_get(self):
        pozycja = self.__polozenie[-1]
        return pozycja
    
    def pos_set(self, new_pos):
        self.__polozenie.append(new_pos)
    
    @property
    def ver_get(self):
        ver = self.__v[-1]
        return ver
    
    def ver_set(self, new_ver):
        self.__v.append(new_ver)

if __name__ == "__main__":
    kulka = Kulka([1], 7, [1])
    x = kulka.pos_get
    print(x)
    kulka.pos_set([2])
    x = kulka.pos_get
    print(x)