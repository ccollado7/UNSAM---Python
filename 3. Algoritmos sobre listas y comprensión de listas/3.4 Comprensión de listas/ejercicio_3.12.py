# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:02:16 2020

@author: User
"""

#Importo el modulo que necesito
import csv


#Defino la Funcion que obtiene los datos del camion
def leer_camion(nombre_archivo):
    ''' Funcion que lee un archivo de cajones en un camion 
        y devuelve una lista de diccionarios donde cada uno 
        de estos corresponde a una fruta '''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            lote = dict(zip(encabezados,fila))
            camion.append(lote)
    return camion

camion = leer_camion('camion.csv')
mas100 = [s for s in camion if int(s['cajones'])>100]
print(mas100)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
print(myn)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

costo10k = [s for s in camion if int(s['cajones']) * float(s['precio']) > 10000]
print(costo10k)

