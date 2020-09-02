# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:10:08 2020

@author: Claudio Collado

"""
#Ejercicio 4.8

import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def tirar(naipes):
    mano = random.sample(naipes,k=3)
    return mano

mano = tirar(naipes)
diccionario_mano = dict(mano)

print(diccionario_mano)





#%%


from collections import Counter
a = Counter(diccionario_mano.values())
mas_comun = a.most_common(1)

if mas_comun[0][1]) = 2:
    
    

valores_validos = [1, 2, 3, 4, 5, 6, 7]
    
#%%
lista_numeros = []
lista_palo = []
for k in mano:
    i,j = k
    lista_numeros.append(i)
    lista_palo.append(j)

print(lista_numeros)
print(lista_palo)



