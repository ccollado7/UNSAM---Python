# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:36:02 2020

@author: Claudio Collado

"""
#Ejercicio 4.8

import random

#Creo un juego de naipes
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(palo,valor) for palo in palos for valor in valores ]


#Funcion N°1
def tirar(naipes):
    '''Funcion que genera una mano aleatoria'''
    mano = random.sample(naipes,k=3)
    return mano

#Funcion N°2
def lista_a_evaluar(mano):
    '''Funcion que recibe una mano aleatoria y devuelve una lista
       para evaluar el tipo de envido'''
    validas = [1, 2, 3, 4, 5, 6, 7]
    lista_oro = []
    lista_copa = []
    lista_espada = []
    lista_basto = []
    for i in mano:
        if (i[0] == 'oro') and (i[1] in validas):
            lista_oro.append(i[1])
        elif (i[0] == 'copa') and (i[1] in validas):
            lista_copa.append(i[1])
        elif (i[0] == 'espada') and (i[1] in validas):
            lista_espada.append(i[1])
        elif (i[0] == 'basto') and (i[1] in validas):
            lista_basto.append(i[1])

    #Creo la lista final que voy a retornar
    lista_final = []
    
    #Condiciones para 'Oro'
    if len(lista_oro) == 3:
        lista_oro = sorted(lista_oro,reverse=True)
        suma_oro = sum(lista_oro[0:2])
        lista_final.append(suma_oro)
    elif len(lista_oro) == 2:
        suma_oro = sum(lista_oro)
        lista_final.append(suma_oro)
    else:
        pass
        
    #Condiciones para 'copa'
    if len(lista_copa) == 3:
        lista_copa = sorted(lista_copa,reverse=True)
        suma_copa = sum(lista_copa[0:2])
        lista_final.append(suma_copa)
    elif len(lista_copa) == 2:
        suma_copa = sum(lista_copa)
        lista_final.append(suma_copa)
    else:
        pass
    
    #Condiciones para 'espada'
    if len(lista_espada) == 3:
        lista_espada = sorted(lista_espada,reverse=True)
        suma_espada = sum(lista_espada[0:2])
        lista_final.append(suma_espada)
    elif len(lista_espada) == 2:
        suma_espada = sum(lista_espada)
        lista_final.append(suma_espada)
    else:
        pass
    
    #Condiciones para 'basto'
    if len(lista_basto) == 3:
        lista_basto = sorted(lista_basto,reverse=True)
        suma_basto = sum(lista_basto[0:2])
        lista_final.append(suma_basto)
    elif len(lista_basto) == 2:
        suma_basto = sum(lista_basto)
        lista_final.append(suma_basto)
    else:
        pass
    
    return lista_final


#Evaluo la ejecucion para un valor N grande y asi poder calcular las probabilidades

N = 100000
sum_31 = 0
sum_32 = 0
sum_33 = 0
for i in range(N):
    mano = tirar(naipes)
    lista_final = lista_a_evaluar(mano)
    if len(lista_final) != 0:
        suma_envido = max(lista_final)
        if suma_envido == 13:
            sum_33 += 1
        elif suma_envido == 12:
            sum_32 +=1
        elif suma_envido == 11:
            sum_31 +=1
    else:
        pass

#Calculo las Probabilidades
prob_31 = sum_31/N
prob_32 = sum_32/N
prob_33 = sum_33/N

#Imprimo las probabilidades
print(f'Podemos estimar la probabilidad de sacar 31 de envido mediante: {prob_31:.4f}.')  
print(f'Podemos estimar la probabilidad de sacar 32 de envido mediante: {prob_32:.4f}.')
print(f'Podemos estimar la probabilidad de sacar 33 de envido mediante: {prob_33:.4f}.')

