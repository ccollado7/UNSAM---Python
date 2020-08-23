# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:10:04 2020

@author: Claudio Collado

"""
#Ejercicio 3.7

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    m = 0 
    for e in lista:
        if e > m:
            m = e
    return m

#Se probaron los siguientes casos:
    #maximo([1,2,7,2,3,4]) -  Resultado 7
    #maximo([1,2,3,4]) - Resultado 4
    #maximo([-5,4]) - Resultado 4
    #maximo([-5,-4] - Resultado 0
    
    
def maximo_corregido(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía '''
    m = lista[0] 
    for e in lista:
        if e > m:
            m = e
    return m

#Se probaron los siguientes casos:
    #maximo_corregido([-5,-4]) - Resultado -4
    #maximo_corregido([-4,-5]) - Resultado -4
    #maximo_corregido([-2,-5,0,-10]) - Resultado 0
    #maximo_corregido([2,-5,0,-10]) - Resultado 2


def minimo(lista):
    '''Devuelve el minimo de una lista, 
    la lista debe ser no vacía '''
    m = lista[0] 
    for e in lista:
        if e < m:
            m = e
    return m

#Se probaron los siguientes casos:
    #minimo([1,2,7,2,3,4]) - Resultado 1
    #minimo([1,2,3,4]) - Resultado 1
    #minimo([-5,4]) - Resultado -5
    #minimo([-5,-4]) - Resultado -5
    
    