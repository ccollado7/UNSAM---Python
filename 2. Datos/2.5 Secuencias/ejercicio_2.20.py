# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:50:39 2020

@author: Claudio Collado

"""
precios = {
    'Pera': 490.1,
    'Lima': 23.45,
    'Naranja': 91.1,
    'Mandarina': 34.23}

lista_precios = list(zip(precios.values(),precios.keys()))


a = [1,2,3,4]
b = ['w','x','y','z']
c = [0.2,0.4,0.6,0.8]

lista = list(zip(a,b,c))

d = [1,2,3,4,5,6]
e = ['x','y','z']

lista_1 = list(zip(d,e))
