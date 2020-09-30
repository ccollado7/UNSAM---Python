# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:23:33 2020

@author: Claudio Collado

"""
#Ejercicio 7.1


from datetime import datetime

def segundos_nacimiento(fecha):
    ''''Funcion que recibe una fecha del tipó dd/mm/AAAA' 
        (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) 
        y te devuelve la cantidad de segundos que viviste'''
        
    fecha_inicio = datetime.strptime(fecha, '%d/%m/%Y') #Fecha de Nacimiento
    fecha_actual = datetime.now() #Fecha Actual
    
    diferencia_fechas = fecha_actual - fecha_inicio #Realizo la diferencia de fechas
    total_segundos = diferencia_fechas.total_seconds() #Transformo a segundos
    
    return int(total_segundos) #Retorno la cantidad de segundos en formato entero

#Pruebas

fecha_1 = segundos_nacimiento('02/04/1985')
print(fecha_1)

fecha_2 = segundos_nacimiento('01/01/2020')
print(fecha_2)

fecha_3 = segundos_nacimiento('01/01/2010')
print(fecha_3)