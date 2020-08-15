# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:46:17 2020

@author: User
"""

precios = {}

with open('precios.csv','rt') as f:
    for line in f:
        try:
            row = line.split(',')
            precios[row[0]] = float(row[1])
        except:
            print('Una linea esta vacia')
print(precios)
    