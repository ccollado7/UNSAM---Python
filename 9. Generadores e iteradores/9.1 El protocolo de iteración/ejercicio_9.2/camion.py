# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:00:17 2020

@author: Claudio Collado

"""
# camion.py

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self._lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total