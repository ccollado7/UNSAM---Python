# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:32:55 2020

@author: Claudio Collado

"""
# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
