# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:06:58 2020

@author: Claudio Collado

"""
def preguntar_edad(nombre):
    edad = int(input(f'Ingresa tu edad {nombre}: '))
    if edad < 0:
        raise ValueError('La edad no puede ser negativa')
    return edad
