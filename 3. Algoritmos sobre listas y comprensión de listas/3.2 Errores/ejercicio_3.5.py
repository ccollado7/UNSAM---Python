# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:16:38 2020

@author: User
"""

#Ejercicio 3.5
#Codigo original

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"r") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("camion.csv")
pprint(camion)

#Resultados de ejecutar el script:
    #[{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
    
#Analsis del Error:
    #Se esta contantemente referenciando a los mismos valores de la fila y esto genera la repeticion
    
#Solucion: 
    #Se realiza la asignacion a un diccionario en una sola operacion
    

def leer_camion_corregido(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"r") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {encabezado[0]:fila[0], encabezado[1]:int(fila[1]),encabezado[2]:float(fila[2])}
            camion.append(registro)
    return camion

camion_corregido = leer_camion_corregido("camion.csv")
pprint(camion_corregido)

#Resultados de ejecutar el script:
    #[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
    #{'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
    #{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
    #{'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
    #{'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
    #{'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
    #{'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
    
