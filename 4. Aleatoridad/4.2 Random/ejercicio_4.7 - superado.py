# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:17:06 2020

@author: Claudio Collado

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

def generala_no_servida():    
    k = 5 #numero de dados
    cnt = 3 #contador de la cantidad de tiros
    acumulado = [] #lista de dados acumulados con los que me quedo
    while (len(acumulado) <5) and (cnt > 0):
        dados = tirar(k) #Llamo a la funcion que tira los dados
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

#print(generala_no_servida())
#print(es_generala(generala_no_servida()))

#%%
N = 1000000
G = sum([es_generala(generala_no_servida()) for i in range(N)])
prob = G/N  
print(prob*100)   


    

