# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:28:39 2020

@author: Claudio Collado

"""
#Ejercicio 3.19

import csv

def leer_arboles(nombre_archivo):
    arboleda = []
    f = open(nombre_archivo,'r',encoding = 'utf8')
    filas = csv.reader(f)
    encabezado = next(filas)
    for fila in filas:
        diccionario_arbol = dict(zip(encabezado,fila))
        arboleda.append(diccionario_arbol)
    return arboleda
    
arboleda = leer_arboles('arbolado-en-espacios-verdes.csv')

H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(H)

