# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:50:47 2020

@author: User
"""

#Ejercicio 4.7

import random

def tirar(k):    
    tirada = []
    for i in range(k):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if len(set(tirada)) == 1:
        return True
    else:
        return False

from collections import Counter


def primera_tirada():
    k = 5
    acumulado = []
    dados = tirar(k)
    contados = Counter(dados).most_common()
    l,m = contados[0]
    for p in range(m):
        acumulado.append(l)
    return acumulado


def generala_no_servida():    
    cnt = 2 #contador de la cantidad de tiros
    acumulado = primera_tirada() #lista de dados acumulados con los que me quedo
    print(acumulado)
    k = 5 - len(acumulado) #Numero de dados a tirar
    while (len(acumulado) <5) and (cnt > 0):
        dados = tirar(k) #Llamo a la funcion que tira los dados
        print(dados)
        if acumulado[0] in dados:
            cantidad = dados.count(acumulado[0])
            cnt_2 = 0
            for p in range(cantidad):
                if len(acumulado) <5:
                    acumulado.append(acumulado[0])
                    cnt_2 = cnt_2 + 1
            k = k - cnt_2
            cnt = cnt - 1
        else:
            contados = Counter(dados).most_common() 
            l,m = contados[0]
            cnt_2 = 0
            for p in range(m):
                if len(acumulado) <5:
                    acumulado.append(l)
                    cnt_2 = cnt_2 + 1
                k = k - cnt_2
                cnt = cnt - 1    
    return acumulado

print(generala_no_servida())

#%%
N = 100000
G = sum([es_generala(generala_no_servida()) for i in range(N)])
prob = G/N  
print(prob*100)
