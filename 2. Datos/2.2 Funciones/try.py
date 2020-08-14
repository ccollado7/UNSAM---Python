# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:58:25 2020

@author: Claudio Collado

"""
numero_valido = False
while not numero_valido:
    try:
        a = input('Ingrese un numero entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es valido.Intenta de nuevo')
print(f'Ingresaste {n}')