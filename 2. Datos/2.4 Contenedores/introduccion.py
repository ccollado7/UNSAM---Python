# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:44:49 2020

@author: Claudio Collado

"""
camion = [
    ('Pera',100,490.1),
    ('Naranja',50,91.3),
    ('Limon',150,83.44)
    ]

print(camion[0])
print(camion[1])

registros = []
registros.append(('Pera',100,490.1))
registros.append(('Naranja',50,91.3))

print(registros)

registros = []
with open('camion.csv','rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        registros.append((row[0],int(row[1]),float(row[2])))
print(registros)

