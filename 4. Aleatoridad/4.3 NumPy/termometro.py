# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:56:01 2020

@author: User
"""
#%%
#Ejercicio 4.11

import random

#Defino una funcion que genera los valores de error
def error():
    '''Esta funcion genera valores numericos distribuidos
       aleatoriamente con media 0 y sigma de 0.2'''
    error = random.normalvariate(0,0.2)
    return error

N = 99
temp = [float(37.5 + error()) for i in range(N)] #Genero una lista 
print(temp) #Imprimo la lista generada

#Maximo    
maximo = max(temp)

#Minimo
minimo = min(temp)

#Promedio
promedio = sum(temp) / N

#Mediana
ordenados = sorted(temp)
def mediana(ordenados):
    '''Esta funcion recibe una seria se valores ordenados de
       menor a mayor y devuelve la mediana de los mismos'''
    if (len (ordenados)) % 2 == 0:
        indice_1 = int((len(ordenados)/2) + 1)
        indice_2 = int(len(ordenados)/2)
        mediana = (ordenados[indice_1] + ordenados[indice_2]) / 2
    else:
        indice = int((len(ordenados)+1) / 2)
        mediana = ordenados[indice]
    return mediana

mediana = mediana(ordenados)

#Imprimo los resultados
print(f'El Maximo de temperatura es {maximo:.4f}.')
print(f'El Minimo de temperatura es {minimo:.4f}.')
print(f'El Promedio de temperatura es {promedio:.4f}.')
print(f'La mediana de temperatura es {mediana:.4f}.')


#Extra
indice_primer_cuartil = int(len(ordenados) * 0.25)
indice_tercer_cuartil = int(len(ordenados) * 0.75)

primer_cuartil = ordenados[indice_primer_cuartil]
tercer_cuartil = ordenados[indice_tercer_cuartil]

print(f'El 1° cuartil de temperatura es {primer_cuartil:.4f}.')
print(f'El 2° cuartil de temperatura coincide con la mediana y es {mediana:.4f}.')
print(f'El 3° cuartil de temperatura es {tercer_cuartil:.4f}.')

#%%
#Ejercicio 4.13

import random
import numpy as np

def error():
    '''Esta funcion genera valores numericos distribuidos
       aleatoriamente con media 0 y sigma de 0.2'''
    error = random.normalvariate(0,0.2)
    return error

N = 999
temp = np.array([float(37.5 + error()) for i in range(N)]) #Genero un array de numpy
np.save('Temperaturas',temp) #Guardo las temperaturas en el archivo 'Temperaturas.npy'


print(temp) #Imprimo las temperaturas

#Maximo    
maximo = temp.max()

#Minimo
minimo = temp.min()

#Promedio
promedio = temp.mean()

#Mediana
mediana = np.median(temp)

#Imprimo los resultados
print(f'El Maximo de temperatura es {maximo:.4f}.')
print(f'El Minimo de temperatura es {minimo:.4f}.')
print(f'El Promedio de temperatura es {promedio:.4f}.')
print(f'La mediana de temperatura es {mediana:.4f}.')


#Extra (no solicitado en las consignas)

primer_cuartil = np.quantile(temp,0.25)
segundo_cuartil = np.quantile(temp,0.5)
tercer_cuartil = np.quantile(temp,0.75)

print(f'El 1° cuartil de temperatura es {primer_cuartil:.4f}.')
print(f'El 2° cuartil de temperatura es {segundo_cuartil:.4f}.')
print(f'El 3° cuartil de temperatura es {tercer_cuartil:.4f}.')