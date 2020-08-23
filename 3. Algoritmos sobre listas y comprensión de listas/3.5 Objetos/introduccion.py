# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:54:54 2020

@author: User
"""

#%%

a = [1,2,3]
b = a
c = [a,b]

print(c)

#%%

a.append(999)
print(a)
print(b)
print(c)

#%%

a = [1,2,3]
b = a
a = [4,5,6]

print(a)
print(b)


#%%

a = [1,2,3]
b = a
print(a is b)

print(id(a))
print(id(b))

#%%

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)
print(a == c)


#%%
a = [2,3,[100,101],4]
b = list(a)
print(a is b)


a.append(5)
print(a)
print(b)

a[2].append(102)
b[2]
print(a[2] is b[2])


#%%

a = [2,3,[100,101],4]
import copy
b = copy.deepcopy(a)
a[2].append(102)
b[2]
print(a[2] is b[2])

#%% 
a = 42
b = 'Hello world'
print(type(a))
print(type(b))


#%%

import math
items = [abs,math,ValueError]
print(items)

print(items[0](-45))
print(items[1].sqrt(2))

try:
    x = int('not a number')
except items[2]:
    print('Failed!')
    
