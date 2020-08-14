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
        try:
            fila = fila.split(',')
            costo_fila = float(fila[1]) * float(fila[2])
            costo = costo + costo_fila
        except ValueError:
            print(f'Cuidado! La fila {fila} tiene valores vacios ')
    return costo
    
costo = costo_camion('missing.csv')
print('Costo Total: ', costo)