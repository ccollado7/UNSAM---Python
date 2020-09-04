# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:48:49 2020

@author: Claudio Collado

"""

#Devolver multiples resultados

def dividir(a,b):
    c = a // b      # Cociente
    r = a % b       # Resto
    return c, r     # Devolver una tupla con c y r

x, y = dividir(37,5) # x = 7, y = 2

z = dividir(37, 5)   # x = (7, 2)

print(x)
print(y)
print(z)

#Variables globales

nombre = 'Dave'

def saludo():
    print('Hola', nombre)
    

