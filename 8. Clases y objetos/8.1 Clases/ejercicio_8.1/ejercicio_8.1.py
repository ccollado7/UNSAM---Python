# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:54:58 2020

@author: User
"""

import lote

a = lote.Lote('Pera',100,490.10)

#%%
print(a.nombre)
print(a.cajones)
print(a.precio)

#%%

b = lote.Lote('Manzana',50,122.34)

c = lote.Lote('Naranja',75,91.75)

print(b.cajones * b.precio)

print(c.cajones * c.precio)

#%%

lotes = [a,b,c]

for c in lotes:
    print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
