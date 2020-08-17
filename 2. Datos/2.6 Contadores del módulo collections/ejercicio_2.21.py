# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:39:09 2020

@author: Claudio Collado

"""
import csv

def leer_camion(nombre_archivo):
    ''' Funcion que lee un archivo de cajones en un camion 
        y devuelve una lista de diccionarios donde cada uno 
        de estos corresponde a una fruta '''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre':row[0],'cajones':int(row[1]),'precio':float(row[2])}
            camion.append(lote)
    return camion   


camion = leer_camion('camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']
    
camion2 = leer_camion('camion2.csv')
from collections import Counter
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']   
