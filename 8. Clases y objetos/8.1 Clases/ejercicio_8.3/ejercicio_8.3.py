# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:47:28 2020

@author: User
"""

import fileparse
with open('camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

#%%

import lote

camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(camion)

print(sum([c.costo() for c in camion]))