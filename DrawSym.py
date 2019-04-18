# -*- coding: utf-8 -*-
import pygame, sys, os
import numpy as np
import random as ran
from pygame.locals import *
#from gracz import Gracz
from pygame.math import Vector2

class DrawSym(object):
    def __init__(self, lista_atomow):
        #config
        self.tps_max = 100.0
        
        #initalisation
        pygame.init()
        
        self.window = pygame.display.set_mode((1000, 1000)) #tworzy okno
        
        self.tps_clock = pygame.time.Clock() #zegar
        self.tps_delta = 0.0
        
        self.lista_pos_at = lista_atomow
        self.kolory = []
        for i in range(len(self.lista_pos_at)):
            self.kolory.append((ran.randrange(255),ran.randrange(255),ran.randrange(255)))
        i = 0
        while True:
            #sprawdza nowe zdarzania
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if i == len(self.lista_pos_at[0]) - 1:
                pygame.quit()
                sys.exit(0)
            #ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            
            #rendering
            self.window.fill((0,0,0))
            self.draw(i)
            pygame.display.flip()
            i += 1
            
    def draw(self, i):
        #rysuje
        for pos, k in zip(self.lista_pos_at, self.kolory):
            postac = pygame.Rect(pos[i][0]+500, pos[i][1]+500, 10, 10)
            pygame.draw.rect(self.window, k, postac)
#        self.player3.prostokat()