# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:28:57 2020

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

d['cajones'] = 75
print(d)

d['fecha'] = (14,8,2020)
d['cuenta'] = 12345
print(d)

for k in d:
    print('k = ',k)

for l in d:
    print(l, '=', d[l])
    
items = d.items()
print(items)

for k,v in items:
    print(k,'=',v)

lista_diccionario = list(d)
print(lista_diccionario)


claves = d.keys()
print(claves)

nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
print(nuevos_items)
d = dict(nuevos_items)
print(d)
