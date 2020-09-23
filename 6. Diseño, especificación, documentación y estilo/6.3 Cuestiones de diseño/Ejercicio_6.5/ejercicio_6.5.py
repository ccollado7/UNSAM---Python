# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:14:07 2020

@author: User
"""

def main(argv):
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = sys.argv[1]
    precios = sys.argv[2]
    return informe_camion(camion, precios)

if name == 'main':
    import sys
    main(sys.argv)