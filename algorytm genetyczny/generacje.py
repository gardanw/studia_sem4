#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

populacja = []
for i in range(20):
    populacja.append(np.random.choice([0,1]))
    
wzor = []
pom = []
for i in range(len(populacja)):
    if i%2 == 0:
        pom.append(1)
    else:
        pom.append(0)
wzor.append(pom)
pom = []
for i in range(len(populacja)):
    if i%2 != 0:
        pom.append(1)
    else:
        pom.append(0)
wzor.append(pom)
print(wzor)
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

populacje_po = []
for i in range(len(reg)):
    populacja_nowa = populacja[:]
#    print(populacja)
    for step in range(500):
        for j in range(len(populacja_nowa)):
            pom = []
            if j < len(populacja_nowa) - 1:
                pom.append(str(populacja_nowa[j-1]))
                pom.append(str(populacja_nowa[j]))
                pom.append(str(populacja_nowa[j+1]))
                klucz = ''.join(pom)
                populacja_nowa[j] = int(reg[i][klucz])
            else:
                pom.append(str(populacja_nowa[j-1]))
                pom.append(str(populacja_nowa[j]))
                pom.append(str(populacja_nowa[0]))
                klucz = ''.join(pom)
                populacja_nowa[j] = int(reg[i][klucz])
#        print(populacja_nowa)
    reg[i]['populacja_po'] = populacja_nowa
    populacje_po.append(populacja_nowa)
for i in populacje_po:
    print(i)

for i in range(len(reg)):
    score = []
    
    for w in range(len(wzor)):
        s = 0
        for j in range(len(reg[i]['populacja_po'])):    
            if reg[i]['populacja_po'][j] == wzor[w][j]:
                s += 1
        score.append(s)
    print(score)
    reg[i]['score'] = max(score)
    
for i in reg:
    print(i)
score = []
for i in reg:
    score.append(i['score'])
print(score)
while len(reg) > 4:
    reg.pop(score.index(min(score)))
    score.pop(score.index(min(score)))

for i in reg:
    print(i)

