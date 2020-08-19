# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:42:21 2020

@author: Claudio Collado
"""

import csv

#Ejercicio 2.22
def leer_parque(nombre_archivo,parque):
    lista_arboles = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            diccionario_arbol = dict(zip(encabezado,fila))
            if diccionario_arbol['espacio_ve'] == parque:
                lista_arboles.append(diccionario_arbol)
    if len(lista_arboles) == 0:
        return(print('Se genero una lista vacia. Por favor verifique que el nombre del parque ingresado sea correcto'))
    else:
        return lista_arboles


#Ejercicio 2.23
def especies(lista_arboles):
    lista_especies = []
    for lista in lista_arboles:
        lista_especies.append(lista['nombre_com']) 
    return set(lista_especies)

    #Ejecucion del Ejercicio 2.23 - Desde consola:
        #lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
        #especies(lista_de_arboles)
        

#Ejercicio 2.24
from collections import Counter

def contar_ejemplares(lista_arboles):
    diccionario_especies = Counter()
    for arbol in lista_arboles:
        diccionario_especies[arbol['nombre_com']] += 1
    return diccionario_especies

     #Ejecucion del Ejercicio 2.24 - Desde consola:
        #lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
        #contar_ejemplares(lista_arboles)     


#Ejercicio 2.25
def obtener_alturas(lista_arboles,especie):
    altura_arboles = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            altura = arbol['altura_tot']
            altura_arboles.append(float(altura))
    maximo = round(max (altura_arboles),2)
    from statistics import mean
    promedio = round(mean(altura_arboles),2)
    print('El maximo es: ' + str(maximo))
    print('El promedio es: ' + str(promedio))
    return (maximo,promedio)

        #Ejecucion del Ejercicio 2.25 - Desde consola:
            #lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
            #obtener_alturas(lista_arboles,especie)

#Ejercicio 2.26
def obtener_inclinaciones(lista_arboles,especie):
    inclinacion_arboles = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion = arbol['inclinacio']
            inclinacion_arboles.append(float(inclinacion))
    return inclinacion_arboles

        #Ejecucion del Ejercicio 2.26 - Desde consola:
            #lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
            #obtener_inclinaciones(lista_arboles,especie)
    
#Ejercicio 2.27
def especimen_mas_inclinado(lista_arboles):
    diccionario = {}
    lista_especies = especies(lista_arboles) #Llamo a la funciones especies()
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie) #Llamo a la funcion obtener_inclinaciones()
        diccionario[max(inclinaciones)] = especie
        valor_maximo = max(diccionario.keys())  
        clave_de_maximo = diccionario[valor_maximo]
    return (clave_de_maximo, valor_maximo)

         #Ejecucion del Ejercicio 2.27 - Desde consola:
            #lista_arboles = leer_parque('arbolado-en-espacios-verdes.csv',parque)
            #especimen_mas_inclinado(lista_arboles)
            
#Ejercicio 2.28
from statistics import mean
def especimen_promedio_mas_inclinado(lista_arboles):
    diccionario = {}
    lista_especies = especies(lista_arboles) #Llamo a la funciones especies()
    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie) #Llamo a la funcion obtener_inclinaciones()
        diccionario[mean(inclinaciones)] = especie
        valor_maximo = max(diccionario.keys())  
        clave_de_maximo = diccionario[valor_maximo]
    return (clave_de_maximo, valor_maximo)

