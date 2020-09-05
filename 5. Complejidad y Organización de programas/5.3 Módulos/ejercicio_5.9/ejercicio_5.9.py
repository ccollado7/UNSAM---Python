# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:25:14 2020

@author: Claudio Collado

"""

import informe_funciones as informe

def costo_camion(nombre_archivo):
    archivo = informe.leer_camion(nombre_archivo)
    costo = 0
    for fila in archivo:
        costo_fila = fila['cajones'] * fila['precio']
        costo = costo + costo_fila
    return costo
    
costo = costo_camion('camion.csv')
print('Costo Total: ', costo)