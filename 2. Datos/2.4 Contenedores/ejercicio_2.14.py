# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:28:20 2020

@author: Claudio Collado

"""

import csv

def leer_precios(nombre_archivo):
    diccionario_precios = {}
    f = open(nombre_archivo,'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            diccionario_precios[row[0]] = float(row[1])
        except:
           print('Fila Vacia')
    return diccionario_precios

        