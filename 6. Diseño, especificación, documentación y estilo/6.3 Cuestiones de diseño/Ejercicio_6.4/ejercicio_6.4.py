# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:46:21 2020

@author: Claudio Collado

"""

#Ejercicio 6.4

import fileparse
import gzip

#%%
with open('missing.csv') as f:
    camion_1 = fileparse.parse_csv(f,select=['nombre', 'cajones'], types = [str, int, float],silence_errors = False)
    
print(camion_1)


#%%
with gzip.open('camion.csv.gz', 'rt') as file:
    camion_2 = fileparse.parse_csv(file, types=[str,int,float])
print(camion_2)

#%%
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion_3 = fileparse.parse_csv(lines, types=[str,int,float])
print(camion_3)

#%%
camion_4 = fileparse.parse_csv('camion.csv', types=[str,int,float])
print(camion_4)
