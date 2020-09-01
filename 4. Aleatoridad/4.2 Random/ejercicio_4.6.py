# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:02:55 2020

@author: Claudio Collado

"""
import random

def tirar():    
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if len(set(tirada)) == 1:
        return True
    else:
        return False
#%%
N = 1000000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#Casos evaluados:
    # N = 100000
        # 90 ocurrencias
        # 67 ocurrencias
        # 84 ocurrencias
        # 75 ocurrencias
        # 76 ocurrencias
        
    # N = 1000000
        # 750 ocurrencias
        # 748 ocurrencias
        # 750 ocurrencias
        # 773 ocurrencias
        # 749 ocurrencias
        
#%%
def pruebas(N,cantidad):
    lista_total = []
    lista_probabilidades = []
    for i in range(cantidad):
        salio_generala_servida = [es_generala(tirar()) for i in range(N)]
        G = sum([es_generala(tirar()) for i in range(N)])
        prob = G/N
        lista_total.append(G)
        lista_probabilidades.append(prob)
        diccionario = dict(zip(lista_total,lista_probabilidades))
    return (diccionario)

#Casos evaluados:
    #pruebas(100000,10)
    #pruebas(100000,50)
    #pruebas(1000000,10)