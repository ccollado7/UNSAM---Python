# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:45:00 2020

@author: User
"""

import fileparse
import gzip
with gzip.open('camion.csv.gz', 'rt') as file:
    camion = fileparse.parse_csv(file,select=['cajones','precio'], types=[str,int,float])

print(camion)

#%%

lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion = fileparse.parse_csv(lines, types=[str,int,float])