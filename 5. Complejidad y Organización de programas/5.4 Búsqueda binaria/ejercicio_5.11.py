# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:53:20 2020

@author: Claudio Collado

"""

#Ejercicio 5.11

def donde_insertar(lista, x):
    '''Funcion que recibe una lista ordenada y un elemento x.
    Si el elemento x se encuentra en la lista devulve el indice de x.
    Si el elemento x no se encuentra en la lista busca el indice donde
    se deberia insertar para no alterar el orden de la lista'''
    
    #Realizo la busqueda binaria
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    #Evaluo si el elemento x fue encontrado por medio de busqueda binaria
    if pos != -1:
        return pos
    else: #Si no lo encuentro busco el indice donde se podria insertar
        for i in lista: #Recorro cada elemento de la lista (peor caso es busqueda lineal O(n))
            if (x > i) and (lista.index(i)<len(lista)-1):
                pass
            else:
                if (lista.index(i) == len(lista)-1) and (x > i):
                    return (lista.index(i)+1)
                else:
                    return lista.index(i)

#Casos Probados:
    #donde_insertar([0,2,4,6], 7) - Resultado 4
    #donde_insertar([0,2,4,6], 2) - Resultado 1
    #donde_insertar([0,2,4,6], 3) - Resultado 2
    #donde_insertar([0,2,4,6], 5) - Resultado 3
    #donde_insertar([0,2,4,6], 6) - Resultado 3          
    #donde_insertar([0,2,4,6], 100) - Resultado 4