# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:13:33 2020

@author: Claudio Collado

"""
#Introduccion

#Documentacion

import random
def elegir_codigo():
    '''Devuelve un codigo de 4 digitos elegido al azar'''
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ""
    for i in range(4):
        candidato = random.choice(digitos)
        # Debemos asegurarnos de no repetir digitos
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo

a = 9.81
b = 5
c = 0.5 * a * b**2

a = 9.81   # Valor de la constante G (aceleración gravitacional), en m/s²
b = 5      # Tiempo en segundos
c = 0.5 * a * b**2  # Desplazamiento (en metros)

#Sobredocumentacion

def buscar_elemento(lista_de_numeros, numero):
    '''Esta función devuelve el índice (contando desde 0) en el que se
       encuentra el número `numero` en la lista `lista_de_numeros`.
       Si el elemento no está en la lista devuelve -1.
    '''
    # Recorremos todos los índices de la lista, desde 0 (inclusive) hasta N
    # (no inclusive)
    for indice in range(len(lista_de_numeros)):
        # Si el elemento en la posicion `indice` es el buscado
        if lista_de_numeros[indice] == numero:
            # Devolvemos el índice en el que está el elemento
            return indice
    # No lo encontramos, devolvemos -1
    return -1

#Sobredocumentacion corregida

def indice(lista, elemento):
    '''Devuelve el índice en el que se encuentra el `elemento` en la `lista`,
       o -1 si no está.
    '''
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

#%%
#Assert

x = 0
assert x != 0, 'El divisor no puede ser 0'

#%%
#Ejemplo N°1 - Division

def division(dividendo, divisor):
    '''Cálculo de la división

    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    assert divisor != 0, 'El divisor no puede ser 0'
    return dividendo / divisor

#%%
#Ejemplo N°2 - Division

def division(dividendo, divisor):
    '''Cálculo de la división

    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    return dividendo / divisor



