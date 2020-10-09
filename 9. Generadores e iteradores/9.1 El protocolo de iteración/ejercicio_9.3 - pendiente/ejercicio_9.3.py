# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:26:31 2020

@author: User
"""

import informe
camion = informe.leer_camion('camion.csv')

#%%

print(len(camion))

#%%

print(camion[0])

#%%

print(camion[1])

#%%

print(camion[0:3])

#%%

print('Naranja' in camion)

#%%

print('Manzana' in camion)
