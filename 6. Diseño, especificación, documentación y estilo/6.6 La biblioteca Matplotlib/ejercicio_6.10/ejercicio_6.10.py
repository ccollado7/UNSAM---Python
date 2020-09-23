# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:13:44 2020

@author: Claudio Collado

"""
#Ejercicio 6.10

#%%
#Item 1

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

plt.plot(randomwalk(N))
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.show()


#%%
#Item 2

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

for i in range(12):
    i = randomwalk(N)
    plt.plot(i)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.show()

#%%
#Item 3

import numpy as np
import matplotlib.pyplot as plt

plt.clf()
fig = plt.figure(figsize=(14,8)) #Dimensiones de la figura


#12 caminatas
plt.subplot(211)
plt.suptitle('12 caminatas al azar',size=20)
def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

lista_valores = [] #Lista para almacenar los valores de cada caminata
lista_maximos = [] #Lista para almacenar los maximos de los valores absolutos  de cada caminata
for i in range(12):
    i = randomwalk(N) #Realizo la caminata
    lista_valores.append(i) #Los valores los incorporo a la lista
    lista_maximos.append(max(abs(i))) #Almaceno los maximos de los valores absolutos de cada caminata
    plt.plot(i) #Ploteo cada caminata
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')


#Caminata mas alejada
maximo = max(lista_maximos) #Me quedo con el maximo
indice = lista_maximos.index(maximo) #Obtengo el indice de ese maximo
maxima_caminata = lista_valores[indice] #Obtengo los valores del indice maximo

plt.subplot(223) #Posicion en la figura
plt.plot(maxima_caminata,color='lightcoral',label='mas alejada') #Ploteo la caminata maxima. Selecciono un color especifo (no coincide con el color de las 12 caminatas juntas)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.legend()


#Caminata menos alejada
minimo = min(lista_maximos) #Me quedo con el minimo
indice = lista_maximos.index(minimo) #Obtengo el indice de ese minimo
minima_caminata = lista_valores[indice] #Obtengo los valores del indice minimo

plt.subplot(224) #Posicion en la figura
plt.plot(minima_caminata,color='lightblue',label='menos alejada') #Ploteo la caminata minima. Selecciono un color especifo (no coincide con el color de las 12 caminatas juntas)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.legend()

plt.show()

