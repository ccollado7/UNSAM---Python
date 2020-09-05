# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:53:20 2020

@author: Claudio Collado

"""

#Ejercicio 5.11

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x):
    pos = busqueda_binaria(lista,x)
    if pos != -1:
        return pos
    else:
        for i in lista:
            if (x > i) and (lista.index(i)<len(lista)-1):
                pass
            else:
                if (lista.index(i) == len(lista)-1) and (x > i):
                    return (lista.index(i)+1)
                else:
                    return lista.index(i)

insertar = donde_insertar([0,2,4,6], 7)
print(insertar)
            
        