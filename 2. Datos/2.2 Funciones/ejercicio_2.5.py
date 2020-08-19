# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:25:14 2020

@author: Claudio Collado

"""
def costo_camion(nombre_archivo):
    archivo = open(nombre_archivo,'rt')
    next(archivo)
    costo = 0
    for fila in archivo:
        fila = fila.split(',')
        costo_fila = float(fila[1]) * float(fila[2])
        costo = costo + costo_fila
    return costo
    
costo = costo_camion('camion.csv')
print('Costo Total: ', costo)