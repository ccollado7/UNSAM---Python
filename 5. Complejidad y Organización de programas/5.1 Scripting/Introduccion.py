# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:22:26 2020

@author: Claudio Collado

"""
#%%
#Definir nombres

def cuadrado(x):
    return x*x

a = 42
b = a + 2
z = cuadrado(b)
print(z)

#%%
# Definir Funciones

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios

preciosviejos = leer_precios('preciosviejos.csv')
preciosnuevos = leer_precios('preciosnuevos.csv')

#%%
def foo():
    import math
    print(math.sqrt(2))
    help(math)

foo()