# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:04:45 2020

@author: Claudio Collado

"""
import csv

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




