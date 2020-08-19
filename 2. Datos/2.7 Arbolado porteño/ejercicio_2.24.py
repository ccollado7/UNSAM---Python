# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:42:21 2020

@author: Claudio Collado
"""

import csv

#Ejercicio 2.22
def leer_parque(nombre_archivo,parque):
    lista_parque = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            diccionario_arbol = dict(zip(encabezado,fila))
            if diccionario_arbol['espacio_ve'] == parque:
                lista_parque.append(diccionario_arbol)
    if len(lista_parque) == 0:
        return(print('Se genero una lista vacia. Por favor verifique que el nombre del parque ingresado sea correcto'))
    else:
        return lista_parque


#Ejercicio 2.23
def especies(lista_arboles):
    lista_especies = []
    for lista in lista_arboles:
        lista_especies.append(lista['nombre_com']) 
    return set(lista_especies)

    #Ejecucion del Ejercicio 2.23 - Desde consola:
        #lista_de_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
        #especies(lista_de_arboles)

#Ejercicio 2.24
from collections import Counter

def contar_ejemplares(lista_de_arboles):
    diccionario_especies = Counter()
    for arbol in lista_de_arboles:
        diccionario_especies[arbol['nombre_com']] += 1
    return diccionario_especies

     #Ejecucion del Ejercicio 2.24 - Desde consola:
        #lista_de_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
        #contar_ejemplares(lista_de_arboles)     

