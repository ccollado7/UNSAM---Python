# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:12:30 2020

@author: Claudio Collado
"""
numero_valido = False
while not numero_valido:
    try:
        a = input('Ingresa un numero entero:' )
        n = int(a)
        numero_valido = True
    except:
        print('No es valido, Intenta de nuevo: ')
print(f'Ingresaste{n}')
