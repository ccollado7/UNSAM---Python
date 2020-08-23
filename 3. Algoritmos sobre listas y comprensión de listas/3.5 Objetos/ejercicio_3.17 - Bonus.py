# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:26:13 2020

@author: Claudio Collado

"""
#Ejercicio 3.17 - Bonus

import csv

f = open('dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)


def fecha_a_tupla(fecha):
    lista = []
    a = fecha.split('/')
    for i in a:
        lista.append(int(i))
    return tuple(lista)


types = [str,float,fecha_a_tupla,str,float,float,float,float,int]
converted = [func(val) for func,val in zip(types,row)]
record = dict(zip(headers,converted))
print(record)
print(record['name'])
print(record['price'])

