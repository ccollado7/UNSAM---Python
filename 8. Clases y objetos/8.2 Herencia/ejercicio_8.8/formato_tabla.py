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

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))    

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')

    def fila(self, data_fila):
        print('<tr><th>'+'</th><th>'.join(data_fila)+'</th></tr>')
        
def crear_formateador(nombre):
    if nombre == 'html':
        formateador = FormatoTablaHTML()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'txt':
        formateador = FormatoTablaTXT()
    return(formateador)