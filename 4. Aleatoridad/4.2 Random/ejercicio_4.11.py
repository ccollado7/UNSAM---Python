# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:49:17 2020

@author: Claudio Collado

"""
import random

def error():
    error = random.normalvariate(0,0.2)
    return error

N = 99
temp = [float(37.5 + error()) for i in range(N)]
print(temp)

#Maximo    
maximo = max(temp)

#Minimo
minimo = min(temp)

#Promedio
promedio = sum(temp) / N

#Mediana
ordenados = sorted(temp)

def mediana(ordenados):
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