# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:22:55 2020

@author: Claudio Collado

"""

import numpy as np

#%%
#Arreglos n-dimensionales

a = np.array([1,2,3,4,5,6])
print(a)

b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(b)

print(a[0])
print(b[0])
print(b[2])
print(b[2][3])
print(b[2,3])

#%%
#Arreglos basicos

a = np.array([1,2,3])

b = np.zeros(2)
print(b)

c = np.ones(2)
print(c)

d = np.empty(2)
print(d)

e = np.arange(4)
print(e)

f = np.arange(2,9,2)
print(f)

g = np.linspace(0,10,num=5)
print(g)

#%%

x = np.ones(2,dtype = np.int64)
print(x)

#%%
#Ordenamiento

arr = np.array([2,1,5,3,7,4,6,8])
print(arr)

print(np.sort(arr))

#%%
#Concatenar

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

concatenado = np.concatenate((a,b))
print(concatenado)

#%%
#Concatenar
x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])

concatenado_1 = np.concatenate((x,y),axis=0)
print(concatenado_1)

#%%
#Dimensiones 

array_ejemplo = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],[[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])

print(array_ejemplo.ndim)
print(array_ejemplo.shape)
print(array_ejemplo.size)

#%%

a = np.arange(6)
print(a)

b = a.reshape(3,2)
print(b)

#%%
#Agregar un nuevo eje a un arreglo

a = np.array([1,2,3,4,5,6])
print(a.shape)

vec_fila = a[np.newaxis,:]
print(vec_fila.shape)

vec_col = a[:,np.newaxis]
print(vec_col.shape)

#%%
#Indices y rebanadas

data = np.array([1,2,3])

print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b[b<5])

five_up = (b >= 5)
print(b[five_up])

pares = b[b % 2 == 0]
print(pares)

c = b[(b>2) & (b<11)]
print(c)

five_up_new = (b>5) | (b == 5)
print(five_up_new)


