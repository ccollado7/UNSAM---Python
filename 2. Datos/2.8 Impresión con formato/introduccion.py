# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:13:57 2020

@author: Claudio Collado

"""

nombre = 'Naranja'
cajones = 100
precio = 91.1

cadena = f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}'

print(cadena)

s = {
     'nombre' : 'Naranja',
     'cajones' : 100,
     'precio' : 91.1
     }


print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s))


print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format(nombre='Naranja', cajones=100, precio=91.1))

print('{:10s} {:10d} {:10.2f}'.format('Naranja', 100, 91.1))

a = 'The value is %d' % 3
print(a)

b = '%5d %-5d %10d' % (3,4,5)
print(b)

c = '%0.2f' % (3.1415926,)
print(c)