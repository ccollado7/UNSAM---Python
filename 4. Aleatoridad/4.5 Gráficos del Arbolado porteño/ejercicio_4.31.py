# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:28:39 2020

@author: Claudio Collado

"""
#Ejercicio 4.31

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

H = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

vector = np.array(H)

altura = vector[:,0]
diametro = vector[:,1]


plt.scatter(diametro,altura,alpha=0.2)
plt.xlabel('diametro (cm)')
plt.ylabel('alto (m)')
plt.title('Relacion diametro-alto para Jacarandás')



