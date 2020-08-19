# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:23:53 2020

@author: Claudio Collado

"""

#Ejercicio 2.34

numero = list(range(10))
tabla = []
for i in range(10):
    fila = [str(i)+':']
    for j in numero:
        resultado = i * j
        fila.append(resultado)
    tabla.append(fila)

encabezado = list(range(10))
cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve = encabezado   
print(f'{cero:>11d} {uno:>5d} {dos:>5d} {tres:>5d} {cuatro:>5d} {cinco:>5d} {seis:>5d} {siete:>5d} {ocho:>5d} {nueve:>5d}') 
print('------------------------------------------------------------------')

for inicio,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve in tabla:
    print(f'{inicio:>5s} {cero:>5d} {uno:>5d} {dos:>5d} {tres:>5d} {cuatro:>5d} {cinco:>5d} {seis:>5d} {siete:>5d} {ocho:>5d} {nueve:>5d}')

#El ejercicio 2.34 muestra directamente en pantalla el resultado (tabla con formato) al presionar F5 en Spyder
