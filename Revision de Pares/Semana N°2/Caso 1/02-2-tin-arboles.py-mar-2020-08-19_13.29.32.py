# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:00:20 2020.

@author: Martin
"""

import csv
from collections import Counter

#%%
def leer_parque(archivo, parque):
    """Lee el archivo y devuelve los arboles del parque."""
    rta = []
    with open(archivo, "r", encoding = "utf8") as arboles:
        rows = csv.reader(arboles)
        headers = next(rows)
        for row in rows:
            if row[10] == parque:
                pos = dict(zip(headers,row))
                rta.append(pos)
    return rta

#%%
def especies(lista_arboles):
    rta = []
    for row in lista_arboles:
        rta.append(row["nombre_com"])
    rta = set(rta)        
    return rta

#%%
def contar_ejemplares(lista_arboles):
    contador = Counter()
    for row in lista_arboles:
        contador[row["nombre_com"]] += 1
    return contador
#%%
arbolParque1 = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
arbolParque2 = leer_parque("arbolado-en-espacios-verdes.csv", "ANDES, LOS")
arbolParque3 = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")

comunes1 = contar_ejemplares(arbolParque1).most_common(5)
comunes2 = contar_ejemplares(arbolParque2).most_common(5)
comunes3 = contar_ejemplares(arbolParque3).most_common(5)

#%%
def obtener_altura(lista_arboles, especie):
    rta = []
    for row in lista_arboles:
        if row["nombre_com"] == especie:
            rta.append(float(row["altura_tot"]))
    return rta


#%%
alt1 = obtener_altura(arbolParque1, "Jacarandá")
alt2 = obtener_altura(arbolParque2, "Jacarandá")
alt3 = obtener_altura(arbolParque3, "Jacarandá")

max1 = max(alt1)
max2 = max(alt2)
max3 = max(alt3)
prom1 = sum(alt1)/len(alt1)
prom2 = sum(alt2)/len(alt2)
prom3 = sum(alt3)/len(alt3)

#%%
def obtener_inclinaciones(lista_arboles, especie):
    rta = []
    for row in lista_arboles:
        if row["nombre_com"] == especie:
            rta.append(float(row["inclinacio"]))
    return rta

#%%
def especimen_mas_inclinado(lista_arboles):
    rta = ["",0]
    esps = especies(lista_arboles)
    for esp in esps:
        maxIncl = max(obtener_inclinaciones(lista_arboles, esp))
        if rta[1] < maxIncl:
            rta[0] = esp
            rta[1] = maxIncl
    return rta
#%%
maxIncl1 = especimen_mas_inclinado(arbolParque1)
maxIncl2 = especimen_mas_inclinado(arbolParque2)
maxIncl3 = especimen_mas_inclinado(arbolParque3)

#%%
def especie_promedio_mas_inclinada(lista_arboles):
    rta = ["",0]
    esps = especies(lista_arboles)
    for esp in esps:
        promIncl = sum(obtener_inclinaciones(lista_arboles, esp))/len(obtener_inclinaciones(lista_arboles, esp))
        if rta[1] < promIncl:
            rta[0] = esp
            rta[1] = promIncl
    return rta

promMax = especie_promedio_mas_inclinada(arbolParque2)









