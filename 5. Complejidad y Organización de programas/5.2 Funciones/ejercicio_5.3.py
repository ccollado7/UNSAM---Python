# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:43:38 2020

@author: Claudio Collado

"""
#Ejercicio 5.3

import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records

camion = parse_csv('camion.csv')
print(camion)