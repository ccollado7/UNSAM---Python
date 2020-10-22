# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:08:28 2020

@author: Claudio Collado

"""

def hojas_ISO(N):
    if N > 10:
        return ('Ingreso un numero erroneo... Recuerde que el tamaño más pequeño corresponde a A10')
    elif N == 0:
        largo = 1189
        ancho = 841
        return (largo,ancho)
    else:
        largo, ancho = hojas_ISO(N-1)
        return (ancho, largo//2)

#%%

print(hojas_ISO(0))
print(hojas_ISO(1))
print(hojas_ISO(2))
print(hojas_ISO(3))
print(hojas_ISO(4))
print(hojas_ISO(5))
print(hojas_ISO(6))
print(hojas_ISO(7))
print(hojas_ISO(8))
print(hojas_ISO(9))
print(hojas_ISO(10))
print(hojas_ISO(12))