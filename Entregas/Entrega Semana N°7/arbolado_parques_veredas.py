# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:34:07 2020

@author: Claudio Collado

"""

#Ejercicio 7.9

#Importo los modulos que voy a necesitar
import pandas as pd
import os


#Item 1

#Lectura del archivo de datos de arboles en parques
directorio_parques = '' #Tengo ubicados los .csv en el mismo lugar que el archivo .py
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_parques = os.path.join(directorio_parques,archivo_parques)
df_parques = pd.read_csv(fname_parques)

#Lectura del archivo de datos de arboles en veredas
directorio_veredas = '' #Tengo ubicados los .csv en el mismo lugar que el archivo .py
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join(directorio_veredas,archivo_veredas)
df_veredas = pd.read_csv(fname_veredas)



#Item 2

#Columnas para arboles en el parque
col_parques = ['altura_tot', 'diametro']

#Columnas para arboles en las veredas
col_veredas = ['altura_arbol', 'diametro_altura_pecho'] 

#DataFrame para tipas en los parques
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'] [col_parques].copy()
df_tipas_parques.rename(columns={'altura_tot': 'altura', 'diametro': 'diametro'},inplace = True)

#DataFrame para tipas en las veredas
df_tipas_veredas =df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'] [col_veredas].copy()
df_tipas_veredas.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'},inplace = True)



#Item 3

#Agrego la columna para el DataFrame de parques
df_tipas_parques['ambiente'] ='parque'

#Agrego la columna para el DataFrame de veredas
df_tipas_veredas['ambiente'] ='vereda'



#Item 4

#Concateno los dos dataframes
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])



#Item 5

df_tipas.boxplot('diametro',by = 'ambiente')



#Item 6

df_tipas.boxplot('altura',by = 'ambiente')


#%%
#Item 7

#Importo los modulos que voy a necesitar
import pandas as pd
import os

#Lectura del archivo de datos de arboles en parques
directorio_parques = '' #Tengo ubicados los .csv en el mismo lugar que el archivo .py
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_parques = os.path.join(directorio_parques,archivo_parques)
df_parques = pd.read_csv(fname_parques)

#Lectura del archivo de datos de arboles en veredas
directorio_veredas = '' #Tengo ubicados los .csv en el mismo lugar que el archivo .py
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join(directorio_veredas,archivo_veredas)
df_veredas = pd.read_csv(fname_veredas)


#Columnas para arboles en el parque
col_parques = ['altura_tot', 'diametro']

#Columnas para arboles en las veredas
col_veredas = ['altura_arbol', 'diametro_altura_pecho'] 

#Defino una funcion que recibe el nombre de la especie en parque y vereda y devuelve el dataframe unificado

def dataframe_especie(nombre_en_parque,nombre_en_vereda):
    '''Funcion que recibe el nombre de la especie en el parque
       y en la vereda y devuelve un dataframe unificado'''
    
    #DataFrame para tipas en los parques
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == nombre_en_parque] [col_parques].copy()
    df_tipas_parques.rename(columns={'altura_tot': 'altura', 'diametro': 'diametro'},inplace = True)
    
    #DataFrame para tipas en las veredas
    df_tipas_veredas =df_veredas[df_veredas['nombre_cientifico'] == nombre_en_vereda] [col_veredas].copy()
    df_tipas_veredas.rename(columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'},inplace = True)
    
    
    #Agrego la columna para el DataFrame de parques
    df_tipas_parques['ambiente'] ='parque'
    
    #Agrego la columna para el DataFrame de veredas
    df_tipas_veredas['ambiente'] ='vereda'
    
    
    #Concateno los dos dataframes
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    return df_tipas


#Realizo la prueba para la especie Jacaranda

dataframe_especie('Jacarandá mimosifolia','Jacaranda mimosifolia').boxplot('diametro',by = 'ambiente')

dataframe_especie('Jacarandá mimosifolia','Jacaranda mimosifolia').boxplot('altura',by = 'ambiente')


