#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as ran
import numpy as np
n = 10
T = 300
siatka = []
for i in range(n):
    linia = []
    for j in range(n):
        pom = ran.randint(0,1)
        if pom == 0:    
            linia.append(-1)
        else:
            linia.append(1)
    siatka.append(linia)

for i in siatka:
    print(i)
H = []
for i in range(len(siatka)):
    linia = []
    for i in range(len(siatka[i])):
        linia.append(0)
    H.append(linia)
eps = 1
for i in range(len(siatka)):
    for j in range(len(siatka[i])):
        if i != len(siatka)-1 and j != len(siatka[i])-1:
            H[i][j] += eps*siatka[i][j]*eps*siatka[i-1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i+1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j-1]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j+1]
        elif i == len(siatka) - 1 and j != len(siatka[i])-1:
            H[i][j] += eps*siatka[i][j]*eps*siatka[i-1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[0][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j-1]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j+1]
        elif i != len(siatka) - 1 and j == len(siatka[i])-1:
            H[i][j] += eps*siatka[i][j]*eps*siatka[i-1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i+1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j-1]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][0]
        elif i == len(siatka) - 1 and j == len(siatka[i])-1:
            H[i][j] += eps*siatka[i][j]*eps*siatka[i-1][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[0][j]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][j-1]
            H[i][j] += eps*siatka[i][j]*eps*siatka[i][0]
suma = 0
for i in range(len(H)):
    suma += sum(H[i])
print(suma)
for i in H:
    print(i)
for k in range(len(siatka)**2):
    siatka_new = siatka[:]
    H_new = H[:]
    x = ran.randrange(len(siatka))
    y = ran.randrange(len(siatka[0]))
    siatka_new[x][y] = siatka_new[x][y]*(-1)
    H_new[x][y] = H_new[x][y]*(-1)
    H_new[x-1][y] += siatka_new[x][y]
    if x < len(H_new)-1:
        H_new[x+1][y] += siatka_new[x][y]
    else:
        H_new[0][y] += siatka_new[x][y]
    H_new[x][y-1] += siatka_new[x][y]
    if y < len(H_new)-1:
        H_new[x][y+1] += siatka_new[x][y]
    else:
        H_new[x][0] += siatka_new[x][y]
    suma_new = 0
    for i in range(len(H_new)):
        suma_new += sum(H_new[i])
    if suma_new < suma:
        H = H_new[:]
        suma = suma_new
        siatka = siatka_new[:]
    else:
        prawdo = ran.random()
        if prawdo > np.exp(-(suma_new - suma)/T):
            H = H_new[:]
            suma = suma_new
            siatka = siatka_new[:]
print(suma)
for i in H:
    print(i)