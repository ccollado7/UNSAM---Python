# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:14:10 2020

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

camion = leer_camion('camion.csv')
nombre_cajones = [(s['nombre'],int(s['cajones'])) for s in camion]
print(nombre_cajones)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

nombres = {s['nombre'] for s in camion}
print(nombres)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

stock = {nombre:0 for nombre in nombres}
print(stock)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

for s in camion:
    stock[s['nombre']] += int(s['cajones'])
print(stock)

print('------------------------------------------------------') #Imprimo una linea de separacion entre comandos

precios = leer_precios('precios.csv')
camion_precios = {nombre:precios[nombre] for nombre in nombres}
print(camion_precios)