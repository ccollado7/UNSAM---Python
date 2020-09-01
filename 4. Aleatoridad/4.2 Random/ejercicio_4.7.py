# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:57:21 2020

@author: Claudio Collado

"""

#Ejercicio 4.7

#Funcion N°1

import random

def tirar(k):  
    '''Esta funcion recibe como paramatro la canrtidad de dados k
       que se quieren tirar y devuelve una lista con los valores
       aleatorios obtenidos'''
    tirada = [] #Creo una lista vacia
    for i in range(k): #Repito este ciclo k veces
        tirada.append(random.randint(1,6)) #Eligo un elementoy lo agrego a la lista
    return tirada #Retorno la lista


#Funcion N°2

def es_generala(tirada):
    '''Esta funcion evalua si la lista recibida como parametro
       corresponde a una generala'''
    if len(tirada) == 5: #Evaluo si el largo de la lista tiene 5 elementos
        return True 
    else:
        return False


#Funcion N°3

from collections import Counter

def primera_tirada():
    '''Esta funcion realiza la 1° tirada de dados
       para comenzar el proceso de obtencion o no
       de una generala no servida'''
    k = 5 #Al ser la 1° tirada comienzo con 5 dados
    acumulado = [] #Creo una lista donde acumulo el numero que mas se repita
    dados = tirar(k) #Tiro los dados
    contados = Counter(dados).most_common() #De la lista obtenida me quedo con aquel de mayor repeticion
    l,m = contados[0] #A la lista original agrego el elemento de mayor repeticion
    for p in range(m):
        acumulado.append(l)
    return acumulado #Retorno la lista con los elementos de mayor repeticion en la 1° tirada

#Funcion N°4

def generala_no_servida():    
    cnt = 2 #contador de la cantidad de tiros - Realizo 2 tiros por que previamente realice la 1° tirada
    acumulado = primera_tirada() #lista de dados obtenidos en la 1° tirada
    k = 5 - len(acumulado) #Numero de dados a tirar para comenzar
    while (len(acumulado) <5) and (cnt > 0): #Condicion para ingresar a la ejecucion de los tiros 
        dados = tirar(k) #Llamo a la funcion que tira los dados
        if acumulado[0] in dados:  #Si el numero que ya tenia en la lista se encuentra en los mismos dados entro
            cantidad = dados.count(acumulado[0]) #Cuentos cuandas veces aparece en esta tirada
            cnt_2 = 0 #Contador que me permite ver junto con k cuandos dados tengo que tirar en la proxima
            for p in range(cantidad): # Agrego el valor a la lista
                if len(acumulado) <5:
                    acumulado.append(acumulado[0]) #Agrego el elemento a la lista
                    cnt_2 = cnt_2 + 1 #Sumo 1 por cada elemento que agrego a la lista
            k = k - cnt_2 #Nuevo valor de dados a tirar
            cnt = cnt - 1 #Disminuyo en 1 las tiradas
        else:
            cnt = cnt - 1 #Si no ingrese en el if entonces disminuyo en 1 las tiradas
    return acumulado #Retorno la lista de numeros


N = 100000
G = sum([es_generala(generala_no_servida()) for i in range(N)])
prob = G/N  
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante: {prob*100:.4f}.')


##Casos evaluados:
    # N = 10000
        # Probabilidad = 4.3300 %
    
    # N = 100000
        # Probabilidad = 4.5370 %
    
    # N = 1000000
        # Probabilidad = 4.5091 %
