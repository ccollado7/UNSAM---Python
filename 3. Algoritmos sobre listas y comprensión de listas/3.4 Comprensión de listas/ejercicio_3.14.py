# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:15:27 2020

@author: Claudio Collado

"""

#Ejercicio 3.14

import csv
f = open('fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)

select = ['nombre','cajones','precio']

indices = [headers.index(ncolumna) for ncolumna in select]
print(indices)


row = next(rows)
record = { ncolumna: row[index] for ncolumna, index in zip(select, indices) } 
print(record)

camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
print(camion)
