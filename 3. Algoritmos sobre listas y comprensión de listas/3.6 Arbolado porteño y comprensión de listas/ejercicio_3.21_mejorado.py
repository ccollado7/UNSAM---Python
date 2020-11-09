# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:31:02 2020

@author: User
"""

#Ejercicio 3.21 - mejorado


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
    

arboleda = leer_arboles('arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


def medidas_de_especies(especies,arboleda):
    
    H = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] in especies]
    #diccionario = {arbol['nombre_com']:H for arbol in arboleda if arbol['nombre_com'] in especies}
    diccionario = {especie:H for especie in especies}
    return diccionario

a = medidas_de_especies(especies,arboleda)


