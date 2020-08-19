# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:23:53 2020

@author: Claudio Collado

"""

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

#Defino la Funcion N°3
def balance(archivo_camion,archivo_precios):
    '''Funcion que calculo el costo del camion,
    el valor de las ventas y el balance'''
    
    #Calculo del costo del camion y del costo de venta
    costo_camion = []
    ventas = []
    camion = leer_camion(archivo_camion) #LLamo a la Funcion N°1
    precios = leer_precios(archivo_precios) #Llamo a la Funcion N°2
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


#Ejercicio 2.30
camion = leer_camion('camion.csv')
precios = leer_precios('precios.csv')

def hacer_informe(camion,precios):
    #Inicio
    lista = []
    for i in camion:
        precio = precios[i['nombre']]
        cambio = precio - float(i['precio'])
        lista_1 = list(i.values())
        lista_1.append(cambio)
        lista.append(tuple(lista_1))
    return lista


#Ejercicio 2.31

informe = hacer_informe(camion,precios)
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
        


    
    