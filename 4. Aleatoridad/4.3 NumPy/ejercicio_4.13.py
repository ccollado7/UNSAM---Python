# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:49:17 2020

@author: Claudio Collado

"""
#Ejercicio 4.13

import random
import numpy as np

def error():
    error = random.normalvariate(0,0.2)
    return error

N = 999
temp = np.array([float(37.5 + error()) for i in range(N)])
np.save('Temperaturas',temp)


print(temp)

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


#Extra

primer_cuartil = np.quantile(temp,0.25)
segundo_cuartil = np.quantile(temp,0.5)
tercer_cuartil = np.quantile(temp,0.75)

print(f'El 1° cuartil de temperatura es {primer_cuartil:.4f}.')
print(f'El 2° cuartil de temperatura es {segundo_cuartil:.4f}.')
print(f'El 3° cuartil de temperatura es {tercer_cuartil:.4f}.')