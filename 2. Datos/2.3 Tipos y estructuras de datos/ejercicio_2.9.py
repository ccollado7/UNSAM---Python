# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:56:31 2020

@author: User
"""

import csv
f = open('camion.csv')
filas = csv.reader(f)
next(filas)
fila = next(filas)

t = (fila[0],int(fila[1]),float(fila[2]))

cost = t[1] * t[2]

print(f'{cost:0.2f}')

t = (t[0],75,t[2])
print(t)

nombre,cajones,precio = t
print(nombre)
print(cajones)
print(precio)

t = (nombre,2*cajones,precio)
print(t)