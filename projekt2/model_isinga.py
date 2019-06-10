#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as ran
import numpy as np
import matplotlib.pyplot as plt

def energy(siatka):
    n = len(siatka[0])
    e = np.zeros([n,n])
    for i in range(len(siatka)):
        for j in range(len(siatka[i])):
            cell = siatka[i][j]
            e[i][j] += cell * siatka[(i + 1) % n][j]
            e[i][j] += cell * siatka[i][(j + 1) % n]
            e[i][j] += cell * siatka[i - 1][j]
            e[i][j] += cell * siatka[i][j - 1]
    return e

n = 10
Tem = np.linspace(0.1, 20, 200)
e_mean = np.zeros(len(Tem))
e_std = np.zeros(len(Tem))
for step in range(len(Tem)):
    T = Tem[step]
    print('step = ', step)
    siatka = np.zeros([n, n])
    for x in range(n):
        for y in range(n):
            siatka[x][y] = ran.choice([-1, 1])
    
    for i in siatka:
        print(i)
    
    H = energy(siatka)

    suma = 0
    for i in range(len(H)):
        suma += sum(H[i])
    print(suma)
    steps = 1000
    energie = np.zeros(steps)
    for k in range(steps):
        siatka_new = siatka[:]
        x = ran.randrange(len(siatka))
        y = ran.randrange(len(siatka[0]))
        siatka_new[x][y] = siatka_new[x][y]*(-1)
        H_new = energy(siatka_new)
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
        energie[k] = suma
    e_mean[step] = np.mean(energie)
    e_std[step] = np.std(energie)
    print(energie)
plt.plot(e_mean)
plt.plot(e_std)
plt.show