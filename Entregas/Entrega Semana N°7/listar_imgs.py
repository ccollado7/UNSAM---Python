# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:21:03 2020

@author: Claudio Collado
"""


import os
import sys

def listar_imgs(argv):
    print ('Dentro de listar_imgs()')
    imagenes=[]
    for root, dirs, files in os.walk("./Data/ordenar"): 
        for name in dirs:
            print(os.path.join(root, name))  
        for name in files:
            print(os.path.join(root, name))  
            if name[-3:] == "png":
                imagenes.append(name)
    return imagenes


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('SOY modulo principal')
        listar_imgs(sys.argv) 
    else:
        print('Solo espero un directorio a la vez. Ingresaste más de uno.')

else:
    print('NO SOY modulo principal')
    listar_imgs("./Data/ordenar")