# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:20:30 2020

@author: User
"""

#Ejercicio 4.10

import random

def genera_evalua_punto():
    x = random.random()
    y = random.random()
    if ((x**2) + (y**2)) < 1:
        return True
    else:
        return False

def estimar_pi(N):
    M = sum([genera_evalua_punto() for i in range(N)])
    pi = 4*(M/N)
    return pi

N = 10000
print(estimar_pi(N))

#Casos evaluados:
    #N = 10000
        # pi = 3.1424
        # pi = 3.1464
        # pi = 3.174
    
    #N = 100000
        # pi = 3.14732
        # pi = 3.1438
        # pi = 3.14212
        
    #N = 1000000
        # pi = 3.140816
        # pi = 3.142192
        # pi = 3.139788
        