# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:40:27 2020

@author: Claudio Collado

"""

#Ordenamiento por seleccion

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p , comp = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
        
        comparaciones += comp
    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    comparaciones = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        comparaciones += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max,comparaciones

#%%
#Ordenamiento por insercion

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
       
    comparaciones = 0   
    
    for i in range(len(lista) - 1):
        comparaciones += 1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comp = reubicar(lista, i + 1)
            comparaciones += comp
    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1

    lista[j] = v
    
    return comparaciones
#%%
#Ordeamiento por burbujeo

def ord_burbujeo(lista):
    comparaciones = 0
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                comparaciones += 1
                #print(comparaciones)
                aux = lista[j];
                lista[j] = lista[j+1];
                lista[j+1] = aux;
    return comparaciones


#%%

#Importo el modulo para realizar la copia de las listas
import copy

#Funcion generadora de listas
import random

def generar_lista(N):
    lista = [random.randint(1,1000) for i in range(N)]
    return lista


#Funcion del Experimento

from statistics import mean 

def experimento(N):
    lista_seleccion = []
    lista_insercion = []
    lista_burbujeo = []
    for i in range(100):
        lista = generar_lista(N)
        lista_seleccion.append(ord_seleccion(copy.deepcopy(lista)))
        lista_insercion.append(ord_insercion(copy.deepcopy(lista)))
        lista_burbujeo.append(ord_burbujeo(copy.deepcopy(lista)))
    
    return mean(lista_seleccion),mean(lista_insercion),mean(lista_burbujeo)

N = 10
print(experimento(N))    
    
    