# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:12:05 2020

@author: Claudio Collado

"""
#Introduccion

def add(x,y):
    return x+y

print(add(3,4))
print(add('Hola', 'mundo'))
print(add('3','4'))

print(add(3,'4'))

#%%

autorizados = ['Claudio','Guillermina']
nombre = 'Miguel'
if nombre not in autorizados:
    raise RuntimeError(f'{nombre} no autorizado')
print('Hola')