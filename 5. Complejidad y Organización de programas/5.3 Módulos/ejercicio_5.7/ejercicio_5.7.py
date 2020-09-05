# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:03:14 2020

@author: User
"""
#%%
#Importo el modulo rebotes

import rebotes

#%%
#Importo el modelo hipoteca

import hipoteca

#%%
#Importo el modulo informe

import informe

informe.balance('camion.csv','precios.csv')

#%% 
#Importo el modulo fileparse

import fileparse

#Leo el archivo camion con select (este archivo tiene header)
camion = fileparse.parse_csv('camion.csv',select=['nombre','cajones','precio'], types=[str,int,float])
print(camion)

#Leo el archivo precios (este archivo no tiene header)
lista_precios = fileparse.parse_csv('precios.csv',types=[str,float], has_headers=False)
print(lista_precios)

#Creo un diccionario con la salida de la llamada a la funcion del modulo
precios = dict(lista_precios)
print(precios)

#%%
#Importo la funcion parse_csv del modulo fileparse


from fileparse import parse_csv
camion = parse_csv('camion.csv', select=['nombre','cajones','precio'], types=[str,int,float])
print(camion)