# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:07:29 2020

@author: Claudio Collado

"""

#Ejercicio 4.15

import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=int)
    return album


#Ejercicio 4.16

def album_incompleto(album):
    if 0 in album:
        return True
    else:
        return False
    

#Ejercicio 4.17

import random
def comprar_figu(figus_total):
    numero_figu = random.randint(1,figus_total)
    return numero_figu


#Ejercicio 4.18

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    condicion = True
    while condicion:
        num_figu = comprar_figu(figus_total)
        album[num_figu - 1] += 1
        condicion = album_incompleto(album)
    return album.sum()

#%%
#Ejercicio 4.19

n_repeticiones = 1000
figus_total = 6
L = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#%%
#Ejercicio 4.20

n_repeticiones = 100
figus_total = 670
L = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

    