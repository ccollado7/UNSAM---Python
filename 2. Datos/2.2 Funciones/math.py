# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:02:17 2020

@author: User
"""

import math
x = math.sqrt(10)
print(x)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
print(len(data))
                         