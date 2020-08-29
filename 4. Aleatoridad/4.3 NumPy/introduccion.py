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

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
e = np.nonzero(d<5)
print(e)
lista_de_coordenadas = list(zip(e[0],e[1]))
print(lista_de_coordenadas)
for coord in lista_de_coordenadas:
    print(coord)
print(d[e])

no_hay = np.nonzero(d == 42)
print(no_hay)

#%%
#Crear arreglos usando datos existentes

a = np.array([1,2,3,4,5,6,7,8,9,10])

arr1 = a[3:8]
print(arr1)

arr1[0] = 44
print(a)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b1 = a[0,:]
print(b1)

b1[0] = 99
print(b1)

print(a)

#Uso del metodo copy()

b2 = a[1,:].copy()
print(b2)

b2[0] = 95
print(b2)

print(a)

#%%
#Operaciones basicas con arreglos

data = np.array([1,2])
ones = np.ones(2,dtype=int)

print(data + ones)
print(data - ones)
print(data * data)
print(data / data)

a = np.array([1,2,3,4])
print(a.sum())

b = np.array([[1,1],[2,2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

#%% 
#Broadcasting

data = np.array([1.0,2.0])
print(data * 1.6)

#%%
#Operaciones un poco mas complejas

data = np.array([1.0,2.0])
print(data.max())
print(data.min()) 
print(data.sum())

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.sum())
print(a.min())

minimo_por_columna = a.min(axis=0)
print(minimo_por_columna)

#%%
#Crear matrices

data =np.array([[1,2],[3,4]])
print(data)

data = np.array([[1,2],[3,4],[5,6]])

print(data[0,1])
print(data[1:3])
print(data[0:2,0])

print(data.max())
print(data.min())
print(data.sum())

data = np.array([[1,2],[5,3],[4,6]])
print(data.max(axis=0))
print(data.max(axis=1))

data = np.array([[1,2],[3,4]])
ones = np.array([[1,1],[1,1]])
print(data + ones)

data = np.array([[1,2],[5,3],[4,6]])
ones_row = np.array([[1,1]])
print(data + ones_row)

ones = np.ones((4,3,2))
print(ones)

uno = np.ones(3)
print(uno)

dos = np.zeros(3)
print(dos)

rng = np.random.default_rng(0)
print(rng.random(3))

uno_1 = np.ones((2,3))
print(uno_1)

dos_1 = np.zeros((3,2))
print(dos_1)

print(rng.random((3,2)))

#%%Guardar y cargar objetos de numpy

a = np.array([1,2,3,4,5,6])

np.save('archivo_1',a)

b = np.load('archivo_1.npy')
print(b)



csv_arr = np.array([1,2,3,4,5,6,7,8])
np.savetxt('archivo_2',csv_arr)

c = np.loadtxt('archivo_2')
print(c)
