# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:28:13 2020

@author: Claudio Collado
"""

import csv
f = open('camion.csv')
rows = csv.reader(f)
headers = next(rows)

headers

for row in rows:
    print(row)

f.close()
