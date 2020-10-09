# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:54:30 2020

@author: Claudio Collado

"""
a = [1,9,4,25,16]

i = a.__iter__()

print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

#%%

f = open('camion.csv')
f.__iter__()

while True:
    print(next(f))
