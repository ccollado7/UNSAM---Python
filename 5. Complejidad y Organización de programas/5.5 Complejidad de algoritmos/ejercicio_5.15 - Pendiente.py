# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:26:26 2020

@author: Claudio Collado

"""

#Ejercicio 5.15

def incrementar(s):
    carry = 1
    l=len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i]==1 and carry==1):
            s[i]=0
            carry=1
        else:
            s[i]=s[i]+carry
            carry=0
    return s

def lista_ceros(n):
    lista_ceros = []
    for i in range(n):
        lista_ceros.append(0)
    return lista_ceros

def lista_unos(n):
    lista_unos = []
    for i in range(n):
        lista_unos.append(1)
    return lista_unos

def listar_secuencias(n):
    lista_final = [lista_ceros(n)]
    lista_inicial = lista_ceros(n)
    while lista_inicial != lista_unos(n):
        lista_inicial = incrementar(lista_inicial)
        print(lista_inicial)
    return lista_final
