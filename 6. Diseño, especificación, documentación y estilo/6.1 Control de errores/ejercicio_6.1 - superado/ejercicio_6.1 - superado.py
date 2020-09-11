# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:10:04 2020

@author: Claudio Collado

"""
#Ejercicio 6.1

import csv

def parse_csv(nombre_archivo, select=False, types=[str,float], has_headers=True,silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if select and not has_headers:
            raise RuntimeError("Para seleccionar, necesito encabezados.")

        if has_headers and select:
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
            for indice,fila in enumerate(filas):
                try: #Intento atrapar una excepcion
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
                except ValueError as e: #Si atrapo la excepcion ingreso aqui
                    if not silence_errors: #Evaluo si quiero sienciar o no los informes de errores
                        print(f'Row {indice}: No pude convertir {fila}. Motivo {e}')
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

camion = parse_csv('missing.csv',select=['nombre', 'cajones'], types = [str, int, float],silence_errors = False)
print(camion)