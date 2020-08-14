# costo_camion.py

archivo = open('camion.csv','rt')
next(archivo)
costo_camion = 0
for fila in archivo:
    fila = fila.split(',')
    costo_fila = float(fila[1]) * float(fila[2])
    costo_camion = costo_camion + costo_fila
print(costo_camion)