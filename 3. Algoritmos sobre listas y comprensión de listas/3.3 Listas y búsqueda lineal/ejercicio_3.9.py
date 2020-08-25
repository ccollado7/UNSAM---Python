# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:02:38 2020

@author: User
"""

#Ejercicio 3.9 - opcion 1

def propagar(lista):
    condicion = True #Condicion para ingresar al while
    lista_modificada = lista.copy() #Utilizo una copia de la lista
    while condicion:
        condicion = False #Modifico la condicion del while para que salga en funcion de que ocurre mas adelante en el codigo
        
        #Recorrido hacia adelante
        for i,j in enumerate(lista_modificada): #Recorro la lista
            if (j == 1) and (i != (len(lista_modificada)-1)): 
                if lista_modificada[i+1] == 0: #Evaluo condicion en la posicion posterior
                    lista_modificada[i+1] = 1 #Modifico valor
                    condicion = True #Si genere una modificacion sigo iterando
            else:
                pass
        
        #Recorrido hacia atras
        for i,j in enumerate(lista_modificada): #Recorro la lista
            if (j == 1) and (i != (len(lista_modificada))) and (i != 0):
                if lista_modificada[i-1] == 0: #Evaluo condicion en la posicion anterior
                    lista_modificada[i-1] = 1 #Modifico valor
                    condicion = True #Si genere una modificacion sigo iterando
            else:
                pass    
            
        #Condicion de finalizacion (o seguir iterando)
        if condicion: #Evaluo si se genero alguna modificacion en ambos recorridos (adelante / atras)
            pass
        else:
            condicion == False #Si no se genero ninguna modificacion salgo del while y retorno la lista     
    return lista_modificada


