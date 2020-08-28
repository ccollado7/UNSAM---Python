# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:32:58 2020

@author: Claudio Collado

"""
#Introduccion

#%%
import random

dado = random.randint(1,6)

print(dado)

#%%
import random
tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))

print(tirada)

#%%

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

print(random.choices(caras,k=5))
