# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:42:12 2020

@author: User
"""

import csv

def leer_precios_nuevo(nombre_archivo):
    diccionario_precios = {}
    f = open(nombre_archivo,'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row) != 0:
            diccionario_precios[row[0]] = float(row[1])
    return diccionario_precios
