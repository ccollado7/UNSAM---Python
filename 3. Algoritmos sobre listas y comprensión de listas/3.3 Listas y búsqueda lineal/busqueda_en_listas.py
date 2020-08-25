# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:58:40 2020

@author: Claudio Collado

"""
#%%
#Ejercicio 3.6

def buscar_u_elemento(lista,e):
    '''Si e está en la lista devuelve la posicion 
    de su ultima aparicion, de lo contrario 
    devuelve -1 '''   
    pos = -1
    for i, z in enumerate(lista):
        if z == e:   
            pos = i
    return pos

#Se probaron los siguientes casos:
    #buscar_u_elemento([1,2,3,2,3,4],1) - Resultado 0
    #buscar_u_elemento([1,2,3,2,3,4],2) - Resultado 3
    #buscar_u_elemento([1,2,3,2,3,4],3) - Resultado 4
    #buscar_u_elemento([1,2,3,2,3,4],5) - Resultado -1



def buscar_n_elemento(lista,e):
    '''Cuenta la cantidad de veces que e
    aparece en la lista'''   
    contador = 0  
    for z in lista:
        if z == e:
            contador += 1
    return contador

#Se probaron los siguientes casos:
    #buscar_n_elemento([1,2,3,2,3,4],1) - Resultado 1
    #buscar_n_elemento([1,2,3,2,3,4],2) - Resultado 2
    #buscar_n_elemento([1,2,3,2,3,4],3) - Resultado 2
    #buscar_n_elemento([1,2,3,2,3,4],5) - Resultado 0

#%%
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

