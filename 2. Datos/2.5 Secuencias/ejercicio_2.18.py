# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:25:14 2020

@author: Claudio Collado
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo,'r')
    archivo = csv.reader(f)
    next(archivo)
    costo = 0
    for n_fila,fila in enumerate(archivo,start=1):
        try:
            costo_fila = float(fila[1]) * float(fila[2])
            costo = costo + costo_fila
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo
