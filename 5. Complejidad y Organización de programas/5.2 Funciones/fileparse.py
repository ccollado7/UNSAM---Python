# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:43:38 2020

@author: Claudio Collado

"""

#%%
#Ejercicio 5.5 - Sin select

import csv

def parse_csv(nombre_archivo, types=[str, int, float]):
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
     
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if types:
                fila = [func(val) for func, val in zip(types, fila) ] 

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

camion = parse_csv('camion.csv')
print(camion)

#%%
#Ejercicio 5.5 - Con Select

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

camion = parse_csv('camion.csv',select=['nombre', 'cajones'],types=[str, int])
print(camion)

#%%
#Ejercicio 5.6

import csv

def parse_csv(nombre_archivo, select=False, types=[str,float], has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if has_headers:
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
                
        if has_headers == False:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                #Conversion de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ] 
                # Armar el diccionario
                registros.append((fila[0],fila[1]))
    return registros

#Pruebo el caso con headers y select
camion = parse_csv('camion.csv',select=['nombre', 'cajones'],types=[str, int])
print(camion)

#Pruebo el caso sin headers
precios = parse_csv('precios.csv', types=[str,float], has_headers=False)
print(precios)
