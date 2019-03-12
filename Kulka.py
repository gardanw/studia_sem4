#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Kulka():
    def __init__(self, pol, m, v):
        self.__polozenie = [pol]
        self.__masa = m
        self.__v = [v]
    
    def poz(self):
        pozycja = self.__polozenie[-1]
        return pozycja


if __name__ == "__main__":
    kulka = Kulka([1], 7, [1])
    print(kulka.poz)