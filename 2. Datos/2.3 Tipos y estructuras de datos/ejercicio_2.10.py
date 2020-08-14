# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:23:20 2020

@author: Claudio Collado

"""
import csv
f = open('camion.csv')
filas = csv.reader(f)
next(filas)
fila = next(filas)


d = {
     'nombre':fila[0],
     'cajones': int(fila[1]),
     'precio': float(fila[2])
     }
print(d)

cost = d['cajones'] * d['precio']
print(cost)


d['cajones'] = 75
print(d)

d['fecha'] = (14,8,2020)
d['cuenta'] = 12345
print(d)
