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

#%%
#Ejercicio 4.21

import random
paquete = []
for i in range(5):
    numero_figu = random.randint(1,670)
    paquete.append(numero_figu)

print(paquete)
#%%
#Ejercicio 4.22

import random
def comprar_paquete(figus_total,figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        numero_figu = random.randint(1,figus_total)
        paquete.append(numero_figu)
    return paquete

print(comprar_paquete(670,5))

#%%
#Ejercicio 4.23

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=int)
    return album

def album_incompleto(album):
    if 0 in album:
        return True
    else:
        return False

import random
def comprar_paquete(figus_total,figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        numero_figu = random.randint(1,figus_total)
        paquete.append(numero_figu)
    return paquete


def cuantos_paquetes(figus_total,figus_paquete):
    album = crear_album(figus_total)
    condicion = True
    paquetes = 0
    while condicion:
        paquete = comprar_paquete(figus_total,figus_paquete)
        paquetes += 1
        for i in paquete:
            album[i - 1] += 1
        condicion = album_incompleto(album)
    return paquetes

print(cuantos_paquetes(670,5))

#%%
#Ejercicio 4.24

n_repeticiones = 10000
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 955.1
    #n_repeticiones = 1000
        #Promedio 954.343
        
#%%
#Ejercicio 4.25

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
L_array = np.array(L)
cumplen = L_array[L_array<=850]

prob = len(cumplen) / n_repeticiones

print(f'La probabilidad de de completar el álbum con 850 paquetes o meno es: {prob*100:.2f}.')