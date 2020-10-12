# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:15:01 2020

@author: Claudio Collado

"""

import lote
peras = lote.Lote('Pera', 100, 490.1)
print(peras)


#%%
import informe
camion = informe.leer_camion('camion.csv')
print(camion)
