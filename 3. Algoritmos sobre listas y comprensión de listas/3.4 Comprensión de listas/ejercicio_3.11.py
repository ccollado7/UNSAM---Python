# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:18:55 2020

@author: Claudio Collado

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
costo = sum([int(s['cajones']) * float(s['precio']) for s in camion])
print(costo)


print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

# Defino la Funcion que obtiene los datos de precios
def leer_precios(nombre_archivo):
    ''' Funcion que lee un archivo de precios y devuelve 
        un diccionario de los mismos'''
    diccionario_precios = {}
    f = open(nombre_archivo,'r')
    filas = csv.reader(f)
    for fila in filas:
        try:
            diccionario_precios[fila[0]] = float(fila[1])
        except:
            pass
            #print('Fila Vacia')
    return diccionario_precios


precios = leer_precios('precios.csv')
valor = sum([int(s['cajones']) * precios[s['nombre']] for s in camion])
print(valor)

