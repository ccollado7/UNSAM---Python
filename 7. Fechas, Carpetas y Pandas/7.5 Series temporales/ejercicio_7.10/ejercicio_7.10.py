# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:01:43 2020

@author: User
"""

import pandas as pd


df = pd.read_csv('OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

#%%

#Busqueda de delta_t y delta_h a mano probando valores hasta encontrar valores que hacen que los dos gráficos se vean lo más similares posible.

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20.2 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
