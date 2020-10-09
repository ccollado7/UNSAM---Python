# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:05:58 2020

@author: Claudio Collado

"""
import informe

informe.informe_camion('camion.csv', 'precios.csv')


#%%

import costo_camion

print(costo_camion.costo_camion('camion.csv'))