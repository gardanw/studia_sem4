#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

populacja = []
for i in range(20):
    populacja.append(np.random.choice([0,1]))

reg = []
while len(reg) != 8:
    pom = np.random.randint(0,255)
    if pom not in reg:
        reg.append(pom)
for i in range(len(reg)):
    reg[i] = bin(reg[i])
    reg[i] = reg[i][2:]
    while  len(reg[i]) != 8:
        reg[i] = '0' + reg[i]
print(reg)

stany = ['000','001','010','011','100','101','110','111']
for i in range(len(reg)):
    slownik = {}
    for j in range(len(reg[i])):
        slownik[stany[j]] = reg[i][j]
    reg[i] = slownik
print(reg)
populacja_nowa = populacja[:]
print(populacja)
#for i in range(len(reg)):
for i in range(500):
    for j in range(len(populacja_nowa)):
        pom = []
        if j < len(populacja_nowa) - 1:
            pom.append(str(populacja_nowa[j-1]))
            pom.append(str(populacja_nowa[j]))
            pom.append(str(populacja_nowa[j+1]))
            klucz = ''.join(pom)
            populacja_nowa[j] = int(reg[0][klucz])
        else:
            pom.append(str(populacja_nowa[j-1]))
            pom.append(str(populacja_nowa[j]))
            pom.append(str(populacja_nowa[0]))
            klucz = ''.join(pom)
            populacja_nowa[j] = int(reg[0][klucz])
    print(populacja_nowa)

