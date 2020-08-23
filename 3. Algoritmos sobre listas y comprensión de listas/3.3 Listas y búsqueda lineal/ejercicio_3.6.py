# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:58:40 2020

@author: Claudio Collado

"""

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

def buscar_n_elemento(lista,e):
    '''Cuenta la cantidad de veces que e
    aparece en la lista'''   
    contador = 0  
    for z in lista:
        if z == e:
            contador += 1
    return contador

#Se probaron los siguientes casos:
    #buscar_u_elemento([1,2,3,2,3,4],1) - Resultado 0
    #buscar_u_elemento([1,2,3,2,3,4],2) - Resultado 3
    #buscar_u_elemento([1,2,3,2,3,4],3) - Resultado 4
    #buscar_u_elemento([1,2,3,2,3,4],5) - Resultado -1

