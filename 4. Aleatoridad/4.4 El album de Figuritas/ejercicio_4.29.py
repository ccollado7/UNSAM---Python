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


#%%
#Ejercicio 4.26

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]

import matplotlib.pyplot as plt
plt.hist(L,bins='auto')

#%%
#Ejercicio 4.27

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=int)
    return album

def album_incompleto(figus_total,album):
    numero_cumple = figus_total*0.10
    num_ceros = list(album).count(0)
    if num_ceros < numero_cumple:
        return False
    else:
        return True

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
        condicion = album_incompleto(figus_total,album)
    return paquetes

n_repeticiones = 1000
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 309.04
    #n_repeticiones = 1000
        #Promedio 310.657
        
#%%
#Ejercicio 4.28 

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=int)
    return album

def album_incompleto(album):
    if 0 in album:
        return True
    else:
        return False

#Con respecto a lo realiza previamente aca modifique el contenido de la funcion
import random
def comprar_paquete(figus_total,figus_paquete):
    figuritas_disponibles = list(range(1,figus_total+1)) #Genero un listado de figuritas
    figuritas = random.sample(figuritas_disponibles,k=figus_paquete) #Tomo 5 sin repeticion
    return figuritas


#Con respecto a lo realiza previamente aca modifique solo el nombre de la funcion
def cuantos_paquetes_sin_repeticion(figus_total,figus_paquete):
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

#%%
#Ejercicio 4.28 - Repeticion del Item 4.24

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes_sin_repeticion(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 936.18
    #n_repeticiones = 1000
        #Promedio 944.527

#%%
#Ejercicio 4.25#Ejercicio 4.28 - Repeticion del Item 4.25

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes_sin_repeticion(figus_total, figus_paquete) for i in range(n_repeticiones)]
L_array = np.array(L)
cumplen = L_array[L_array<=850]

prob = len(cumplen) / n_repeticiones

print(f'La probabilidad de de completar el álbum con 850 paquetes o meno es: {prob*100:.2f}.')

#%%
#Ejercicio 4.28 - Repeticion del Item 4.26

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes_sin_repeticion(figus_total, figus_paquete) for i in range(n_repeticiones)]

import matplotlib.pyplot as plt
plt.hist(L,bins='auto')

#%%
#Ejercicio 4.28 - Repeticion del Item 4.27

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=int)
    return album

def album_incompleto(figus_total,album):
    numero_cumple = figus_total*0.10
    num_ceros = list(album).count(0)
    if num_ceros < numero_cumple:
        return False
    else:
        return True

import random
def comprar_paquete(figus_total,figus_paquete):
    figuritas_disponibles = list(range(1,figus_total+1)) #Genero un listado de figuritas
    figuritas = random.sample(figuritas_disponibles,k=figus_paquete) #Tomo 5 sin repeticion
    return figuritas

def cuantos_paquetes_sin_repeticion(figus_total,figus_paquete):
    album = crear_album(figus_total)
    condicion = True
    paquetes = 0
    while condicion:
        paquete = comprar_paquete(figus_total,figus_paquete)
        paquetes += 1
        for i in paquete:
            album[i - 1] += 1
        condicion = album_incompleto(figus_total,album)
    return album

n_repeticiones = 1000
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes_sin_repeticion(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 307.56
    #n_repeticiones = 1000
        #Promedio 308.884

#%%
#Ejercicio 4.29 - Con repeticion

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
    album_1 = crear_album(figus_total)
    album_2 = crear_album(figus_total)
    album_3 = crear_album(figus_total)
    album_4 = crear_album(figus_total)
    album_5 = crear_album(figus_total)
    album_repetidos = crear_album(figus_total)
    condicion = True
    paquetes = 0
    while condicion:
        paquete = comprar_paquete(figus_total,figus_paquete)
        paquetes += 1
        for i in paquete:
            if album_1[i - 1] != 1:
                album_1[i - 1] += 1
            elif album_2[i - 1] != 1:
                album_2[i - 1] += 1
            elif album_3[i - 1] != 1:
                album_3[i - 1] += 1
            elif album_4[i - 1] != 1:
                album_4[i - 1] += 1
            elif album_5[i - 1] != 1:
                album_5[i - 1] += 1
            else:
                album_repetidos[i - 1] += 1
        condicion = album_incompleto(album_1) or album_incompleto(album_2) or album_incompleto(album_3) or album_incompleto(album_4) or album_incompleto(album_5)               
    return paquetes

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 2031.45
    
#%%
#Ejercicio 4.29 - Sin repeticion

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
    figuritas_disponibles = list(range(1,figus_total+1)) #Genero un listado de figuritas
    figuritas = random.sample(figuritas_disponibles,k=figus_paquete) #Tomo 5 sin repeticion
    return figuritas


def cuantos_paquetes_sin_repeticion(figus_total,figus_paquete):
    album_1 = crear_album(figus_total)
    album_2 = crear_album(figus_total)
    album_3 = crear_album(figus_total)
    album_4 = crear_album(figus_total)
    album_5 = crear_album(figus_total)
    album_repetidos = crear_album(figus_total)
    condicion = True
    paquetes = 0
    while condicion:
        paquete = comprar_paquete(figus_total,figus_paquete)
        paquetes += 1
        for i in paquete:
            if album_1[i - 1] != 1:
                album_1[i - 1] += 1
            elif album_2[i - 1] != 1:
                album_2[i - 1] += 1
            elif album_3[i - 1] != 1:
                album_3[i - 1] += 1
            elif album_4[i - 1] != 1:
                album_4[i - 1] += 1
            elif album_5[i - 1] != 1:
                album_5[i - 1] += 1
            else:
                album_repetidos[i - 1] += 1
        condicion = album_incompleto(album_1) or album_incompleto(album_2) or album_incompleto(album_3) or album_incompleto(album_4) or album_incompleto(album_5)               
    return paquetes

n_repeticiones = 100
figus_total = 670
figus_paquete = 5

L = [cuantos_paquetes_sin_repeticion(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(L)
print(promedio)

#Casos probados:
    #n_repeticiones = 100
        #Promedio 2019.3