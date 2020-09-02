# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:05:42 2020

@author: PPEREZ
"""


def propagar(lista):
    propagado = []
    propagado_derecha = []
    propagado_izquierda = []
    propaga = False
    #propaga a la derecha
    for e in lista:
        if e == 1:
            propaga = True
        if e == -1:
            propaga = False
        if e != -1 and propaga == True:
            propagado_derecha.append(1)
        else:
            propagado_derecha.append(e)

    #propago a la izquierda
    propaga = False
    for e in reversed(lista):
        if e == 1:
            propaga = True
        if e == -1:
            propaga = False
        if e != -1 and propaga == True:
            propagado_izquierda.append(1)
        else:
            propagado_izquierda.append(e)        
    propagado_izquierda = propagado_izquierda[::-1]
    
    for i  in range(len(lista)):
        if propagado_derecha[i] == 1 or propagado_izquierda[i] == 1:
            propagado.append(1)
        else:
            propagado.append(lista[i])
    return propagado

print (propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))


#%% Revision de Pares - Casos de prueba evaluados

# Caso 1: [1,0,0,0]
    #Resultado: [1, 1, 1, 1] (Correcto)
    
# Caso 2: [0,-1,0,0,1]
    #Resultado: [0, -1, 1, 1, 1] (Correcto)
    
# Caso 3: [0,-1,0,-1,1]
    #Resultado: [0,-1,0,-1,1] (Correcto)   
    
# Caso 4: [0 for x in range(10)]
    #Resultado: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (Correcto)  

# Caso 5: [1 for x in range(100)]
    #Resultado: [1, 1, 1, 1, 1, 1, 1, ,1] (Correcto)  
    
# Caso 6: [(x%3)-1 for x in range(30)]
    #Resultado: [-1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1] (Correcto)


