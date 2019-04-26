#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Potencjal import Harmoniczny as Har, Langevin as Lv, LennardJones as Lj
#from Potencjal import Langevin as Lv
from Algorytmy import LeapFrog as LF
from Uklad import Uklad
from Kulka import Kulka
from DrawSym import DrawSym as ds
import pygame, sys
import numpy as np
import matplotlib.pyplot as plt
import random as ran

def impacts(lista_kulek, key = 'von Neumanna'):
    '''
    Przyjmuje lista obiektow typu Kulka i klucz typu string.
    Mozliwe klucze: 
    "von Neumanna" -  tworzy wiazania z sasiadami
    "all" - tworzy wiazania miedzy wszystkimi obiektami
    '''
    im = []
    pom = int((len(lista_kulek))**(1/2))
    if key == 'all':
        for i in lista_kulek:
            for j in lista_kulek:
                if i != j and {i,j} not in im:
                    im.append({i,j})
        for i in range(len(im)):
            im[i] = list(im[i])
    elif key == 'von Neumanna':
        for i in range(len(lista_kulek)):
            if i+ pom < len(lista_kulek):
                im.append([lista_kulek[i], lista_kulek[int(i+pom)]])
            else:
#                print(i % pom, i)
                im.append([lista_kulek[i],lista_kulek[i % pom]])
            if (i+1)% np.sqrt(len(lista_kulek)) != 0:
                im.append([lista_kulek[i], lista_kulek[i+1]])
            else:
                im.append([lista_kulek[i], lista_kulek[int(i - pom +1)]])
    return im

class Symulacje():
    def __init__(self, uklad, potencjal, algorytm, steps = 5000):
        self.__uklad = uklad
        self.__potencjal = potencjal
        self.__algorytm = algorytm
        self.__steps = steps
        
        #config
        self.tps_max = 100.0
        
        #initalisation
        pygame.init()
        
        self.window = pygame.display.set_mode((500, 500)) #tworzy okno
        
        self.tps_clock = pygame.time.Clock() #zegar
        self.tps_delta = 0.0
        
        self.kolory = []
        for i in range(len(self.__uklad.kulka_get)):
            self.kolory.append((ran.randrange(255),ran.randrange(255),ran.randrange(255)))
        
    def run(self):
        for i in range(self.__steps):
            f = np.zeros((len(self.__uklad.kulka_get), self.__uklad.dim_get))
            for p in self.__potencjal:
                f += p.calc_forces(self.__uklad)
#            print(f)
            self.__algorytm.ruch(f, self.__uklad.kulka_get)
            print(self.__uklad.kulka_get[0].pos_get[0], self.__uklad.kulka_get[1].pos_get[1], 5, 5)
        # testtuje
        return True
    
    def drawrun(self):
        while True:
            #sprawdza nowe zdarzania
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                    
            f = np.zeros((len(self.__uklad.kulka_get), self.__uklad.dim_get))
            for p in self.__potencjal:
                f += p.calc_forces(self.__uklad)
#            print(f)
            self.__algorytm.ruch(f, self.__uklad.kulka_get)
            
            #ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            
            #rendering
            self.window.fill((0,0,0))
            self.draw()
            pygame.display.flip()
    
    def draw(self):
        #rysuje
        odl_pom = kulki[-1].pos_get_all[0][0] / (len(kulki)**(1/2) - 1)
        for atom, kolor in zip(self.__uklad.kulka_get, self.kolory):
#            print(atom.pos_get[0], atom.pos_get[1])
            postac = pygame.Rect(atom.pos_get[0]+odl_pom/2, atom.pos_get[1]+odl_pom/2, 5, 5)
            pygame.draw.rect(self.window, kolor, postac)
#        self.player3.prostokat()
    
if __name__ == "__main__":
    kulki = []
    n = 10
    id = 0
    for i in range(n):
        for j in range(n):
            kulki.append(Kulka(np.array([j*25, i*25]), 1, np.array([0,0]), idk = id))
            id += 1
    print('ilosc atomow =', id)

    uklad = Uklad(kulki, dim = len(kulki[0].pos_get), T = 3000, imp = impacts(kulki))
    
    # tworzenie listy potencjalow
    pot = []
#    pot.append(Har(k = 1, x0 = 25))
    pot.append(Lv(tarcie=0.3))
    pot.append(Lj(r0 = 25, eps=1))
    
    alg = LF()
    sym = Symulacje(uklad, pot, alg, steps=1)
    # symulacja z wizualizacja
    sym.drawrun()
    
    # symulacja bez wizualizacji
#    sym.run()
    
    # wizualizacja po symylacji
#    lista_pos = []
#    for i in range(len(kulki)):
#        lista_pos.append(kulki[i].pos_get_all)
#    print(lista_pos)
#    ds(lista_pos)
    