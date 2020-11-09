# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:55:44 2020

@author: User
"""

from vigilante import vigilar
import csv
import formato_tabla
import informe

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
        
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
            
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    
    return rows

def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    log = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(log, camion)
    colnames = ['Nombre', 'Precio', 'Volumen']
    
    return formato_tabla.imprimir_tabla(filas, colnames, fmt)
