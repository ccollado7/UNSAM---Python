# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:25:14 2020

@author: Claudio Collado

"""
#Ejercicio 5.9

import informe_funciones as informe #Importo el modulo informe_funciones como informe (informe_funciones.py es un archivo externo a este programa)

def costo_camion(nombre_archivo):
    archivo = informe.leer_camion(nombre_archivo)
    costo = 0
    for fila in archivo:
        costo_fila = fila['cajones'] * fila['precio']
        costo = costo + costo_fila
    return costo
    
costo = costo_camion('camion.csv')
print('Costo Total: ', costo)
