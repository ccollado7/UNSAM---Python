# camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    headers = next(filas)
    costo = 0
    for fila in filas:
        try:
            costo_fila = float(fila[1]) * float(fila[2])
            costo = costo + costo_fila
        except ValueError:
            print(f'Cuidado! La fila {fila} tiene valores vacios ')
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo Total: ', costo)
