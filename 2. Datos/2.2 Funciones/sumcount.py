# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:55:29 2020

@author: Claudio Collado
"""

def sumcount(n):
    '''Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)
print(a)