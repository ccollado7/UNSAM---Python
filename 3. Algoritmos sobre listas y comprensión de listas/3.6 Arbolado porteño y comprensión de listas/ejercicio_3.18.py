# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:28:39 2020

@author: Claudio Collado

"""
#Ejercicio 3.18

import csv

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            diccionario_arbol = dict(zip(encabezado,fila))
            arboleda.append(diccionario_arbol)
        return arboleda
    
    