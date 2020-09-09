# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:36:59 2020

@author: Claudio Collado

"""
#Ejercicio 5.16

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve la cantidad de comparaciones que realizó el algoritmo para encontrarlo o decidir que no está
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        comps+=1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            #Modificacion con respecto al programa original. Si coincide con el valor directamente lo devuelve
            return pos,comps  
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,comps

print(busqueda_binaria([1,2,3,4,5,6,7,9,10],5,verbose=True))