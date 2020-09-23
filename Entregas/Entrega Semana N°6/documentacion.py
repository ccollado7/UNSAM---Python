# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:48:45 2020

@author: Claudio Collado

"""
#Ejercicio 6.8

#%%
#Caso 1

def valor_absoluto(n):
    '''Calculo del valor absoluto
       Pre: Recibe un numero n entero o flotante.
       Pos: Devuelve un entero o flotanto como resultado del valor absoluto.'''
    if n >= 0:
        return n
    else:
        return -n
    
# a) Contrato de la función: 
     #El valor n correspondera a un numero entero o flotante. La funcion devolvera el modulo del valor ingresado
# b) Agregale la documentación adecuada.
# c) Comentá el código si te parece que aporta.
# d) No existe invariantes de ciclo

#%%
#Caso 2

def suma_pares(l):
    '''Calculo de la suma de los enteros pares
       Pre: Recibo un iterable con numeros enteros
       Pos: Devuelve la suma de los enteros pares o 0 en caso contrario o si no se ingresa un iterable'''
    res = 0 #Inicializo la suma en 0
    for e in l: #Recorre cada elemento de l
        if e % 2 ==0: #Si la division entera por 2 da 0 sumo el valor de ese elemento a la variable res
            res += e
        else: 
            res += 0
    return res

# a) Contrato de la función: 
     #El valor l es un iterable que contiene numeros enteros
     #La funcion devuelve la suma de los numeros pares si estos existes o 0 en caso contrario o que no se ingrese un iterable
# b) Agregale la documentación adecuada.
# c) Comentá el código si te parece que aporta.
# d) Invariantes de ciclo: Al iniciar cada ciclo la variable res contiene la suma de los numeros pares anteriores

#%%
#Caso 3

def veces(a, b):
    '''Calcula la suma del numero a consigo mismo b veces
       Pre: Se reciben: a numero entero (positivo y negativo) y b numero entero positivo (incluido el 0 si no quiero sumar)
       Pos: Devuelve la suma de a repetidad b veces'''
    res = 0 #Inicializo en cero la viariable que acumula la suma 
    nb = b
    while nb != 0: #Repito el ciclo hasta que nb sea cero
        #print(nb * a + res)
        res += a #Si ingreso al ciclo sumo el valor de a
        nb -= 1 #Si ingreso al ciclo resto 1 al valor del contador nb
    return res

# a) Contrato de la función: 
     #El valor de a y b son numeros enteros
     #La funcion devuelve la suma de b veces del valor a
# b) Agregale la documentación adecuada.
# c) Comentá el código si te parece que aporta.
# d) Invariantes de ciclo: Al iniciar cada ciclo la variable res contiene la suma del numero a hasta ese ciclo

#%%
#Caso 3

def collatz(n):
    '''Calcula la cantidad de ciclos hasta lograr que el valor n sea 1
       por operaciones de division o transformacion a un numero par
       Pre: Se recibe un numero n entero positivo (distinto de 0)
       Pos: Devuelve la cantidad de veces que se ejecuto el ciclo hasta lograr que n sea 1'''
    res = 1
    while n!=1: #Mientras n sea distinto de 1 ejecuto el ciclo
        if n % 2 == 0: #Evaluo si n es par
            n = n//2 #Si n es par realizo la division entera
        else:
            n = 3 * n + 1 #Si n no es par realio esta operacion para transformalo a par
        res += 1 #En cada ciclo ejecutado sumo 1 al contador
    return res

# a) Contrato de la función: 
     #El valor de n es un numero entero positivo distinto de cero
     #La funcion devuelve el valor de la cantidad de ciclos que se ejecutaron hasta lograr que ese valor sea 1
# b) Agregale la documentación adecuada.
# c) Comentá el código si te parece que aporta.
# d) Invariantes de ciclo: Al iniciar cada ciclo la variable res contiene la cantidad de veces que se ejecuto el ciclo

