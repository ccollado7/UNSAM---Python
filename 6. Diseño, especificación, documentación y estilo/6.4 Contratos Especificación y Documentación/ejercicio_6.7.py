# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:33:28 2020

@author: User
"""

#Ejercicio 6.6. - Opcion 1

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    for i in range(desde,hasta+1):
        suma += i
    
    return suma

suma = sumar_enteros(1,10)
print(suma)

#El invariante del ciclo en este caso corresponde a que la variable suma, al momento de iniciar un ciclo
#contiene la suma de los enteros desde el comienzo hasta ese momento 
