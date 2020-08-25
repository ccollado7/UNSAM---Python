# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:37:21 2020

@author: Claudio Collado

"""

#solucion_de_errores.py

#%%
#Ejercicio 3.1: Semantica
#Codigo Original

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

#Resultados de los casos de test:
    # tiene_a('UNSAM 2020') retorna FALSE
    # tiene_a('abracadabra') retorna TRUE
    # tiene_a('La novela 1984 de George Orwell') retorna FALSE

#Analsis del Error:
    #El error es SEMANTICO ya que el programa no hace lo que está diseñado para hacer
    #Devuelve True solo si la primera letra es una 'a', caso contrario devuelve False
    #El error se produce por incluir el return False al evaluar la condicion de la primera letra

#Solucion: Se modifica el codigo de forma tal que devuelva False en caso que ninguna letra sea 'a'

def tiene_a_corregido(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

#%%
#Ejercicio 3.2: Sintaxis
#Codigo Original

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

#Resultados de los casos de test:
    # tiene_a('UNSAM 2020') genera un error SyntaxError: invalid syntax
    # tiene_a('abracadabra') genera un error SyntaxError: invalid syntax
    # tiene_a('La novela 1984 de George Orwell') genera un error SyntaxError: invalid syntax

#Analsis del Error:
    #El error es de SINTAXIS
    #Errores encontrados:
        #En la definicion de la funcion (def) falto incluir los dos puntos : al final
        #En el while faltan los dos puntos : al final
        #En la comparacion del if se coloca = cuando debe ser ==
        #En el in faltan los dos puntos : al final
        #Al return final se le asocia Falso cuando este no corresponde a un Booleano. Corresponde retornar False

#Solucion: Se corrigen los errores indicados anteriormente

def tiene_a_corregido(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

#%%
#Ejercicio 3.3: Tipos
#Codigo original

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#Resultados de los casos de test:
    # tiene_uno('UNSAM 2020') devuelve False
    # tiene_uno('La novela 1984 de George Orwell') devuelve True
    # tiene_uno(1984) devuelve TypeError: object of type 'int' has no len()
    
#Analsis del Error:
    #El error es de TIPO ya que se intenta obtener el largo de un int
    #Tambien esta el error que no se puede iterar sobre un int

#Solucion: La solucion en este caso es por especificar que el paramtro de la funcion debe ser un string tiene_uno('1984')

#%%
#Ejercicio 3.4: Alcances
#Codigo original

def suma(a,b):
    c = a + b
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#Resultados de ejecutar el script:
    #La suma da 2 + 3 = 0

#Analsis del Error:
    #La funcion suma(a,b) realiza el calculo pero no devuelve el valor de c. El resultado de la suma queda LOCAL en la funcion
    #La impresion de resultado muestra los valores de las variables a,b y c definidos previo al llamado de la funcion
    
#Solucion: 
    #Se incorpora el comando return c en la funcion
    #Se asocia la funcion suma(a,b) a la variable c
    #Opcional: La primera asignacion c = 0 tambien se puede eliminar o dejarla definida PREVIO a la llamada de la funcion


def suma_corregido(a,b):
    c = a + b
    return c
    
c = 0
a = 2
b = 3
c = suma_corregido(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5 - Pisando memoria
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