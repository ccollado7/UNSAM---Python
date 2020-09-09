# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:48:54 2020

@author: Claudio Collado

"""
#Ejercicio 5.14

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

'''Considero que incrementar(s) tiene una complejidad lineal
ya que se recorre cada elemento de la lista en el bucle for. 
Dentro del bucle for se realizan operaciones elementales:
evaluacion de condicional, modificacion del valor de una 
lista,etc.'''