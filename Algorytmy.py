#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Algorytmy:
    def update_pose(self):
        pass
    
    def update_ver(self):
        pass
    
class LeapFrog(Algorytmy):
    def __init__(self, dt=0.01):
        self.__dimension = 1
        self.__tarcie = 0.9
        self.__dt = dt
        
    def update_pos(self, new_pos, kulka):
        kulka.pos_set(new_pos)
    
    def update_ver(self, new_ver, kulka):
        kulka.ver_set(new_ver)
    
    def ruch(self, force, kulki):
        f=force
        odl_pom = kulki[-2].pos_get_all[0][0] / ((len(kulki)/2)**(1/2) - 1)
        # petla wykonywana dla kazdej kulki
        for j in range(len(kulki)):
            new_ver = kulki[j].ver_get + f[j]*self.__dt
            new_pos = kulki[j].pos_get + new_ver*self.__dt
         
            # pseldo wszechswiat
            if new_pos[0] < -odl_pom/2:
                new_pos[0] += (kulki[-1].pos_get_all[0][0] + odl_pom)
            if new_pos[0] > kulki[-1].pos_get_all[0][0] + odl_pom/2:
                new_pos[0] = -odl_pom/2
            if new_pos[1] < -odl_pom/2:
                new_pos[1] += (kulki[-1].pos_get_all[0][0] + odl_pom)
            if new_pos[1] > kulki[-1].pos_get_all[0][0] + odl_pom/2:
                new_pos[1] = -odl_pom/2
            
            # zmiana predkosci i polozenia
            self.update_ver(new_ver, kulki[j])
            self.update_pos(new_pos, kulki[j])
            
            
        
