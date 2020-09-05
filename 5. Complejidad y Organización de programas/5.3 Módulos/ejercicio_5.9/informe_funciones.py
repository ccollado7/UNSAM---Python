# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:23:53 2020

@author: Claudio Collado

"""
#Ejercicio 5.1

#Importo el modulo que necesito
import csv

#Defino la Funcion N°1
def leer_camion(nombre_archivo):
    ''' Funcion que lee un archivo de cajones en un camion 
        y devuelve una lista de diccionarios donde cada uno 
        de estos corresponde a una fruta '''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            fila = [fila[0],int(fila[1]),float(fila[2])]
            lote = dict(zip(encabezados,fila))
            camion.append(lote)
    return camion                    


# Defino la Funcion N°2
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

# Defino la Funcion N°3
def hacer_informe(camion,precios):
    '''Funcion que recibe una lista de diccionarios con la fruta 
       y un diccionario de precios y devuelve una lista de tuplas
       para ser utilizados en la elaboracion de la tabla final'''
    lista = []
    for i in camion:
        precio = precios[i['nombre']]
        cambio = precio - float(i['precio'])
        lista_1 = list(i.values())
        lista_1.append(cambio)
        lista.append(tuple(lista_1))
    return lista


# Defino la Funcion N°4
def imprimir_informe(informe):
    '''Funcion que recibe una lista de tuplas y devuelve
       una tabla con formato'''
    nombre, cajones, precio, cambio = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10s}') 
    print('---------- ---------- ---------- ----------')      
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')


                     
    