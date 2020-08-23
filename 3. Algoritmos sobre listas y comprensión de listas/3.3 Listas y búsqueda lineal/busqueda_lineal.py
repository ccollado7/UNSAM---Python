# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:09:01 2020

@author: Claudio Collado

"""
#Busqueda Lineal

#%%
[1,3,5,7].index(5)

[1,3,5,7].index(20)

5 in [1,3,5,7]

20 in [1,3,5,7]

#%%
def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos

#%%

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos


#%%

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos