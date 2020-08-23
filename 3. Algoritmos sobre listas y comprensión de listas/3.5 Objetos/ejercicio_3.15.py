# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:59:01 2020

@author: Claudio Collado

"""
#Ejercicio 3.15

types = [str,int,float]

import csv
f = open('camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

print(types[1](row[1]))

print(types[2](row[2]))

print(types[1](row[1]) * types[2](row[2]))

r = list(zip(types,row))
print(r)

converted = []
for func, val in zip(types,row):
    converted.append(func(val))
print(converted)

converted_1 = [func(val) for func,val in zip(types,row)]
print(converted)