# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:03:55 2020

@author: Claudio Collado

"""
#Ejercicio 5.13 - Comparacion de soluciones Ejercicio 4.3 y 4.4

#%%
#Ejercicio 4.3: Propagar por vecinos

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m

'''Esta solucion tiene complejidad lineal O(n) ya que en la funcion propagar_al_vecino(l) 
recorre la totalidad de la lista analizando los condicionales IF para ver si tiene que 
propagar a los vecinos'''


#%%
#Ejercicio 4.4: Propagar por como el auto fantástico

def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp

