# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:04:45 2020

@author: Claudio Collado

"""
import csv

def leer_parque(nombre_archivo,parque):
    lista_parque = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if row[10] == parque:
                fila = dict(zip(headers,row))
                lista_parque.append(fila)
    if len(lista_parque) == 0:
        return(print('Se genero una lista vacia. Por favor verifique que el nombre del parque ingresado sea correcto'))
    else:
        return (lista_parque)






