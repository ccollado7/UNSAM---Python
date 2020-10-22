# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:44:35 2020

@author: Claudio Collado

"""
def pascal(n, k):
    #Condicion para el extremo superior
    if n == 0 or k == 0:
        res = 1
        return res
    #Condicion para los extremos distintos de la punta que son 1
    elif (k == 0) or (k == n ):
        res = 1
        return res 
    else:
        res = pascal(n-1, k-1) + pascal(n-1, k)
        return res

#%%

#Prueba de la funcion recursiva en un valor especifico

print(pascal(5,2))


#%%

#Extra
#Defino una funcion que calcula la piramide de pascal hasta el valor de fila n inclusive

def pascal_completo(n):
    lista_pascal = []
    for i in range(n+1):
        lista = [pascal(i,k) for k in range(i+1)]
        lista_pascal.append(lista)
    return lista_pascal
    
print(pascal_completo(5))

