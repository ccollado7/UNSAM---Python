# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:45:18 2020

@author: Claudio Collado

"""
#Ejercicio 3.8

def invertir_lista(lista):
    '''Invierte una lista no vacia'''
    invertida = []
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida

#Se probaron los siguientes casos:
    #[1, 2, 3, 4, 5] -  Resultado [5, 4, 3, 2, 1]
    # ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'] 
         #Resultado ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
        
