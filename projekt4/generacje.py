#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def gener(populacja_nowa, reg, f = False):
    for j in range(len(populacja_nowa)):
        pom = []
        if j < len(populacja_nowa) - 1:
            pom.append(str(populacja_nowa[j-1]))
            pom.append(str(populacja_nowa[j]))
            pom.append(str(populacja_nowa[j+1]))
            klucz = ''.join(pom)
            if f:
               print(klucz, int(reg[klucz]), populacja_nowa[j])
            populacja_nowa[j] = int(reg[klucz])
        else:
            pom.append(str(populacja_nowa[j-1]))
            pom.append(str(populacja_nowa[j]))
            pom.append(str(populacja_nowa[0]))
            klucz = ''.join(pom)
#            print(klucz, int(reg[klucz]), populacja_nowa[j])
            populacja_nowa[j] = int(reg[klucz])
    return populacja_nowa

populacja = []
for i in range(50):
    populacja.append(np.random.choice([0,1]))
    
#populacja = [1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0]
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


stany = ['000','001','010','011','100','101','110','111']
for i in range(len(reg)):
    slownik = {}
    for j in range(len(reg[i])):
        slownik[stany[j]] = reg[i][j]
    reg[i] = slownik

scoress = []
for generacje in range(50):
    populacje_po = []
    for i in range(len(reg)):
        populacja_nowa = populacja[:]
    #    print(populacja)
        for step in range(500):
            populacja_nowa = gener(populacja_nowa, reg[i])
    #        print(populacja_nowa)
        reg[i]['populacja_po'] = populacja_nowa
        populacje_po.append(populacja_nowa)
    
    for i in range(len(reg)):
        s = 0
        for j in range(len(reg[i]['populacja_po'])):
            if j != len(reg[i]['populacja_po']) - 1:
                if reg[i]['populacja_po'][j-1] != reg[i]['populacja_po'][j] and reg[i]['populacja_po'][j+1] != reg[i]['populacja_po'][j]:
                    s += 1
            else:
                if reg[i]['populacja_po'][j-1] != reg[i]['populacja_po'][j] and reg[i]['populacja_po'][0] != reg[i]['populacja_po'][j]:
                    s += 1
        reg[i]['score'] = s
    
    score = []
    for i in reg:
        score.append(i['score'])
    while len(reg) > 4:
        reg.pop(score.index(min(score)))
        score.pop(score.index(min(score)))
    for i in reg:
        scoress.append(i['score'])
    mutacja = np.random.choice(stany)
    reg_mut = copy.deepcopy(np.random.choice(reg))
    if reg_mut[mutacja] == '0':
        reg_mut[mutacja] = '1'
    elif reg_mut[mutacja] == '1':
        reg_mut[mutacja] = '0'
    reg.append(reg_mut)
    
    reg1 = copy.deepcopy(np.random.choice(reg))
    reg2 = copy.deepcopy(np.random.choice(reg))
    while reg1 == reg2:
        reg2 = copy.deepcopy(np.random.choice(reg))
    
    reg3 = copy.deepcopy(np.random.choice(reg))
    for i in range(len(stany)):
        pom = []
        pom.append(reg1[stany[i]])
        pom.append(reg2[stany[i]])
        reg3[stany[i]] = np.random.choice(pom)
        reg1[stany[i]] = np.random.choice(['0', '1'])
        reg2[stany[i]] = np.random.choice(['0', '1'])
    
    reg.append(reg1)
    reg.append(reg2)
    reg.append(reg3)

    
score = []
for i in reg:
    score.append(i['score'])

reg_naj = reg[score.index(max(score))]
print(reg_naj)
populacja_nowa = populacja
print(populacja_nowa)
for i in range(500):
    populacja_nowa = gener(populacja_nowa, reg_naj)
    print(populacja_nowa)

plt.plot(scoress)