# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:28:39 2020

@author: Claudio Collado

"""
#Ejercicio 4.32

import csv
import numpy as np
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo,'r',encoding = 'utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            diccionario_arbol = dict(zip(encabezado,fila))
            arboleda.append(diccionario_arbol)
        return arboleda
    

arboleda = leer_arboles('arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


def medidas_de_especies(especies,arboleda):
    diccionario = {}
    for especie in especies:
        H = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccionario [especie]= H
    return diccionario

diccionario = medidas_de_especies(especies,arboleda)

#%%
#Eucalipto

especie = 'Eucalipto'
datos = diccionario[especie]
vector = np.array(datos)
altura = vector[:,0]
diametro = vector[:,1]
plt.scatter(diametro,altura,alpha=0.2,label = 'Eucalipto')
plt.title('Relacion diametro-altura para ' + especie)
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')
plt.legend()
         
#%%
#Palo borracho rosado

especie = 'Palo borracho rosado'
datos = diccionario[especie]
vector = np.array(datos)
altura = vector[:,0]
diametro = vector[:,1]
plt.scatter(diametro,altura,alpha=0.2, label = 'Palo borracho rosado')
plt.title('Relacion diametro-altura para ' + especie)
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')
plt.legend()
         

#%%
#Palo borracho rosado

especie = 'Jacarandá'
datos = diccionario[especie]
vector = np.array(datos)
altura = vector[:,0]
diametro = vector[:,1]
plt.scatter(diametro,altura,alpha=0.2, label='Jacarandá')
plt.title('Relacion diametro-altura para ' + especie)
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')
plt.legend()

#%%
#Extra 2 especies - Eucalipto y Palo borracho rosado

#Eucalipto

especie_1 = 'Eucalipto'
datos_1 = diccionario[especie_1]
vector_1 = np.array(datos_1)
altura_1 = vector_1[:,0]
diametro_1 = vector_1[:,1]
plt.scatter(diametro_1,altura_1,alpha=0.2, label = 'Eucalipto')

#Palo borracho rosado

especie_2 = 'Palo borracho rosado'
datos_2 = diccionario[especie_2]
vector_2 = np.array(datos_2)
altura_2 = vector_2[:,0]
diametro_2 = vector_2[:,1]
plt.scatter(diametro_2,altura_2,alpha=0.2,label = 'Palo borracho rosado')

plt.title('Relacion diametro-altura para Eucalipto y Palo borracho rosado')
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')         
plt.legend()

#%%
#Extra 2 especies - Eucalipto y Jacarandá

#Eucalipto

especie_1 = 'Eucalipto'
datos_1 = diccionario[especie_1]
vector_1 = np.array(datos_1)
altura_1 = vector_1[:,0]
diametro_1 = vector_1[:,1]
plt.scatter(diametro_1,altura_1,alpha=0.2, label = 'Eucalipto')

#Jacarandá

especie_2 = 'Jacarandá'
datos_2 = diccionario[especie_2]
vector_2 = np.array(datos_2)
altura_2 = vector_2[:,0]
diametro_2 = vector_2[:,1]
plt.scatter(diametro_2,altura_2,alpha=0.2,label = 'Jacarandá')

plt.title('Relacion diametro-altura para Eucalipto y Jacarandá')
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')         
plt.legend()

#%%
#Extra 2 especies - Jacarandá y Palo borracho rosado

especie_1 = 'Jacarandá'
datos_1 = diccionario[especie_1]
vector_1 = np.array(datos_1)
altura_1 = vector_1[:,0]
diametro_1 = vector_1[:,1]
plt.scatter(diametro_1,altura_1,alpha=0.2, label = 'Jacarandá')

#Palo borracho rosado

especie_2 = 'Palo borracho rosado'
datos_2 = diccionario[especie_2]
vector_2 = np.array(datos_2)
altura_2 = vector_2[:,0]
diametro_2 = vector_2[:,1]
plt.scatter(diametro_2,altura_2,alpha=0.2,label = 'Palo borracho rosado')

plt.title('Relacion diametro-altura para Jacarandá y Palo borracho rosado')
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')         
plt.legend()

#%%
#Extra - 3 especies

#Eucalipto

especie_1 = 'Eucalipto'
datos_1 = diccionario[especie_1]
vector_1 = np.array(datos_1)
altura_1 = vector_1[:,0]
diametro_1 = vector_1[:,1]
plt.scatter(diametro_1,altura_1,alpha=0.2, label = 'Eucalipto')

# Jacarandá

especie_2 = 'Jacarandá'
datos_2 = diccionario[especie_2]
vector_2 = np.array(datos_2)
altura_2 = vector_2[:,0]
diametro_2 = vector_2[:,1]
plt.scatter(diametro_2,altura_2,alpha=0.2,label = 'Jacarandá')

#Palo borracho rosado

especie_3 = 'Palo borracho rosado'
datos_3 = diccionario[especie_3]
vector_3 = np.array(datos_3)
altura_3 = vector_3[:,0]
diametro_3 = vector_3[:,1]
plt.scatter(diametro_3,altura_3,alpha=0.2,label = 'Palo borracho rosado')

plt.title('Relacion diametro-altura para las 3 especies')
plt.xlabel('Diametro (cm)')
plt.ylabel('Alto (m)')         
plt.legend()








