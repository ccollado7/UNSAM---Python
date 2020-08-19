# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:03:53 2020

@author: User
"""

import csv


def leer_parque(nombre_archivo,parque):
    lista_parque = []
    listado_de_parques = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            listado_de_parques.append(row[10])
        try:
            if parque in listado_de_parques:
                for row in rows:
                    if row[10] == parque:
                        fila = dict(zip(headers,row))
                        lista_parque.append(fila)
        except:
            print('Se introdujo un nombre de parque erroneo')
    return lista_parque