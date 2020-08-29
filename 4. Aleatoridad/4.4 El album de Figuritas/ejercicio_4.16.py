# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:07:29 2020

@author: Claudio Collado

"""
#%%
#Ejercicio 4.15

import numpy as np

def crear_albun(figus_total):
    albun = np.zeros(figus_total,dtype=int)
    return albun

albun = crear_albun(670)
print(len(albun))

#%%
#Ejercicio 4.16

def albun_incompleto(albun):
    if 0 in albun:
        return True
    else:
        return False
    