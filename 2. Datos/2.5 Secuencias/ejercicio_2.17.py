# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:31:36 2020

@author: User
"""

data = [4,9,1,25,16,100,49]

print('Minimo: ',min(data))
print('Maxio: ',max(data))
print('Suma: ',sum(data))

for x in data:
    print(x)

for n,x in enumerate(data, start=1):
    print(n,x)

for n in range(len(data)):
    print(data[n])