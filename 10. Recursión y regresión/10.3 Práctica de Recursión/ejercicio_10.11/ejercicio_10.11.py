# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:42:29 2020

@author: Claudio Collado
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if (lista[medio]==e):
            res = True
        else:
	        if e < lista[medio]:
	           res = bbinaria_rec(lista[:medio],e)
	        else:
	           res = bbinaria_rec(lista[medio+1:],e)

    return res
	
#%%

lista_prueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(bbinaria_rec(lista_prueba, 3))
print(bbinaria_rec(lista_prueba, 13))
print(bbinaria_rec(lista_prueba, 45))