# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:23:53 2020

@author: Claudio Collado

"""
#Ejercicio 5.8

import fileparse #Importo el modulo fileparse (fileparse.py es un archivo externo a este programa)

#Defino la Funcion N°1
def leer_camion(nombre_archivo):
    '''Funcion que recibe el nombre de un archivo
       y utiliza el modulo fileparse para devolver
       una lista de diccionarios'''
    camion = fileparse.parse_csv(nombre_archivo,types=[str, int,float]) #Utilizo fileparse dentro de la funcion
    return camion                    

# Defino la Funcion N°2
def leer_precios(nombre_archivo):
    '''Funcion que recibe el nombre de un archivo
       y utiliza el modulo fileparse para devolver
       una lista de tuplas'''
    precios = fileparse.parse_csv(nombre_archivo, types=[str,float], has_headers=False) #Utilizo fileparse dentro de la funcion
    diccionario_precios = {}
    for precio in precios:
        try:
            diccionario_precios[precio[0]] = float(precio[1])
        except:
            pass
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


#Realizo la llamada a las funciones creadas anteriormente para obtener la tabla con formato final

camion = leer_camion('camion.csv')
precios = leer_precios('precios.csv')
informe = hacer_informe(camion,precios)
imprimir_informe(informe)


                     
    