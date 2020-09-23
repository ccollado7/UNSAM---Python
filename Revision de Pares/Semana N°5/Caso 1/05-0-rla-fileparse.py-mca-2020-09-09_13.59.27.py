# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:03:39 2020

@author: mcarl
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers= None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, 
    que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f) # Lee los encabezados del archivo
        registros = []
        if has_headers ==False: # si no tiene encabezados,genera tuplas
            for fila in filas: 
                if not fila: 
                    continue #saltea las filas vacias
                if types: 
                     fila=[func(val)for func, val in zip(types,fila)]
                     tupla = tuple(fila) #convierto a tuplas las filas del archivo
                else: 
                    tupla = tuple(fila)
                registros.append(tupla)
        else: # si tiene encabezados, hace diccionarios
            encabezados = next(filas) 
            if select: # Si se indicó un selector de columnas 
                indices = [encabezados.index(nombre_columna) for nombre_columna in select] # busca los índices de las columnas especificadas. 
                encabezados = select # achica el conjunto de encabezados para diccionarios
            else:
                indices = []
            for fila in filas:
                if not fila:    
                    continue # Saltear filas vacías
                if indices: # Filtrar la fila si se especificaron columnas
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ] # convierte los tipos correspondientes
                registro = dict(zip(encabezados, fila))
                registros.append(registro)         
    return registros

#cajones_retenidos = parse_csv('Data/camion.csv', select=['nombre','cajones'])
#camion = parse_csv('Data/camion.csv', types=[str, int, float])
#precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)

#%%

camion_1 = parse_csv('camion.csv', types=[str, int, float])
print(camion_1)

#%%
camion_2 = parse_csv('camion.csv', types=[str, str, str])
print(camion_2)

#%%
camion_3 = parse_csv('camion.csv', select = ['nombre', 'cajones'], types=[str, int])
print(camion_3)

