# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:13:31 2020

@author: Claudio Collado
"""

def ord_burbujeo(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux = lista[j];
                lista[j] = lista[j+1];
                lista[j+1] = aux;
    return lista
 
#%%
#Prueba del algoritmo de ordenamiento por burbuja con los casos provistos

lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

print(ord_burbujeo(lista_1))
print(ord_burbujeo(lista_2))
print(ord_burbujeo(lista_3))
print(ord_burbujeo(lista_4))
print(ord_burbujeo(lista_5))

#%%

#La complejidad del ordenamiento por burbuja es O(n^2). Esto se deduce ya que el algoritmo tiene 2 bucles encadenados
