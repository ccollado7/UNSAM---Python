# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:09:58 2020

@author: Claudio Collado

"""

import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote =(row[0],int(row[1]),float(row[2]))
            camion.append(lote)
    return camion                    
