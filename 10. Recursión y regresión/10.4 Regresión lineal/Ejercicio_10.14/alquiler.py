# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:42:09 2020

@author: Claudio Collado

"""
import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

recta = superficie*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('Ajuste lineal')
plt.plot(superficie, recta, c = 'red')
plt.xlabel('Superficie')
plt.ylabel('Alquiler')

plt.show()


#%%

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())


