# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:09:58 2020

@author: Claudio Collado

"""

import csv

#Funcion N°1

def leer_camion(nombre_archivo):
    ''' Funcion que lee un archivo de cajones en un camion 
        y devuelve una lista de diccionarios donde cada uno 
        de estos corresponde a una fruta '''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {'nombre':row[0],'cajones':int(row[1]),'precio':float(row[2])}
            camion.append(lote)
    return camion                    


#Funcion N°2

def leer_precios(nombre_archivo):
    ''' Funcion que lee un archivo de precios y devuelve 
        un diccionario de los mismos'''
    diccionario_precios = {}
    f = open(nombre_archivo,'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            diccionario_precios[row[0]] = float(row[1])
        except:
            pass
            #print('Fila Vacia')
    return diccionario_precios

#Funcion N°3
def balance(archivo_camion,archivo_precios):
    #Calculo del costo del camion y del costo de venta
    costo_camion = []
    ventas = []
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    for i in camion:
        costo = int(i['cajones']) * float(i['precio'])
        costo_camion.append(costo)
        
        venta = int(i['cajones']) * precios[i['nombre']]
        ventas.append(venta)
        
    suma_costo = sum(costo_camion)
    suma_ventas = sum(ventas)

    #Impresiones por pantalla
    print('El costo del camion es: ', suma_costo)
    print('Las ventas del camion fueron: ', suma_ventas)
    resultado = suma_ventas - suma_costo
    if resultado > 0:
        print('El resultado es positivo de: ', round(resultado,2))
    else:
        print('El resultado es negativo de: ', round(resultado,2))
