# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:43:38 2020

@author: Claudio Collado

"""

import csv

#Ejercicio 5.5 - SELECT / TYPES

def parse_csv(nombre_archivo, select=None, types=None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(ncolumna) for ncolumna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            #Conversion de tipo
            if types:
                fila = [func(val) for func, val in zip(types, fila) ] 
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

camion_1 = parse_csv('camion.csv',select=['nombre', 'cajones'],types=[str, int]) #SELECT y TYPES
print(camion_1)

print('------------------------------------------------')

camion_2 = parse_csv('camion.csv',select=['nombre', 'cajones']) #SELECT
print(camion_2)

print('------------------------------------------------')

camion_3 = parse_csv('camion.csv',types=[str, int,float]) #TYPES
print(camion_3)

print('------------------------------------------------')

camion_4 = parse_csv('camion.csv') #No se incorpora ningun parametro
print(camion_4)

#%%
#Ejercicio 5.6

import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo,'r') as f:
        filas = csv.reader(f)

        if not has_headers:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                #Conversion de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ] 
                # Armar el diccionario
                registros.append((fila[0],fila[1]))

        else:
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(ncolumna) for ncolumna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                #Conversion de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ] 
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)

    return registros

camion_1 = parse_csv('camion.csv',select=['nombre', 'cajones'],types=[str, int]) #SELECT y TYPES / HAS_HEADERS por default es True
print(camion_1)

print('------------------------------------------------')

camion_2 = parse_csv('camion.csv',select=['nombre', 'cajones']) #SELECT / HAS_HEADERS por default es True
print(camion_2)

print('------------------------------------------------')

camion_3 = parse_csv('camion.csv',types=[str, int,float]) #TYPES / HAS_HEADERS por default es True
print(camion_3)

print('------------------------------------------------')

camion_4 = parse_csv('camion.csv') #No se incorpora ningun parametro / HAS_HEADERS por default es True
print(camion_4)

print('------------------------------------------------')
print('------------------------------------------------')
print('------------------------------------------------')

precios_1 = parse_csv('precios.csv', types=[str,float], has_headers=False) #TYPES y HAS_HEADERS
print(precios_1)

print('------------------------------------------------')

precios_2 = parse_csv('precios.csv', has_headers=False) #HAS_HEADERS
print(precios_2)

