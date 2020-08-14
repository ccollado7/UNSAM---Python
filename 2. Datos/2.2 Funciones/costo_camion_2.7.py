# costo_camion.py

import csv
archivo = open('camion.csv')
filas = csv.reader(archivo)
encabezado = next(filas)
costo_camion = 0
for fila in filas:
    costo_fila = float(fila[1]) * float(fila[2])
    costo_camion = costo_camion + costo_fila
print(costo_camion)