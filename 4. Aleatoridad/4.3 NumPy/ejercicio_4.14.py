# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:44:53 2020

@author: Claudio Collado

"""
#Ejercicio 4.14

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('Temperaturas.npy')
plt.hist(temperaturas,bins=25)

