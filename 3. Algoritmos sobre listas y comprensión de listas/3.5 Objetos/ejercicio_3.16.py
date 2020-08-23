# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:17:08 2020

@author: Claudio Collado

"""
#Ejercicio 3.16

types = [str,int,float]

import csv
f = open('camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

converted = []
for func, val in zip(types,row):
    converted.append(func(val))
print(converted)

print(headers)
print(converted)

diccionario = dict(zip(headers,converted))
print(diccionario)

diccionario_1 = {name:func(val) for name,func,val in zip(headers,types,row)}
print(diccionario_1)
