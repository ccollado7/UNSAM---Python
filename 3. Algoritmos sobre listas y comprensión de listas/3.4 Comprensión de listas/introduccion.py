# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:49:07 2020

@author: Claudio Collado

"""
a = [1,2,3,4,5]
b = [2*x for x in a]
print(b)

nombres = ['Edmundo','Juana']
c = [nombre.lower() for nombre in nombres]
print(c)

a = [1,-5,4,2,-2,10]
b = [2*x for x in a if x>0]
print(b)

frutas = [s['nombre'] for s in camion]

a = [s for s in camion if s['precio']>100 and s['cajones']>50]

costo = sum([s['cajones'] * s['precio'] for s in camion])

resultado = []
for variable in secuencia:
    if condicion:
        resultado.append(expresion)