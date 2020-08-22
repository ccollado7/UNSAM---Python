# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:16:09 2020

@author: Claudio Collado

"""
#Ejercicio 3.10

nums = [1,2,3,4]

cuadrados = [x*x for x in nums]
print(cuadrados)

dobles = [2*x for x in nums if x>2]
print(dobles)