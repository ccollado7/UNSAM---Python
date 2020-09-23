#fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)
            if select:
                # Si se indicó un selector de columnas,
                #    buscar los índices de las columnas especificadas.
                # Y en ese caso achicar el conjunto de encabezados para diccionarios
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
                
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    if types:
                        fila = [tipo(fila[index]) for index,tipo in zip(indices,types)]
                    else:
                        fila = [fila[index] for index in indices]
    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [tipo(elem) for tipo,elem in (zip(types, fila))]
                # Agregar la tupla
                registro = tuple(fila)
                registros.append(registro)
    return registros

#%%

camion_1 = parse_csv('camion.csv', types=[str, int, float])
print(camion_1)

#%%
camion_2 = parse_csv('camion.csv', types=[str, str, str])
print(camion_2)

#%%
camion_3 = parse_csv('camion.csv', select = ['nombre', 'cajones'], types=[str, int])
print(camion_3)


#%%
camion_4 = parse_csv('camion.csv', types=[str, str, float])
print(camion_4)


#%%
camion_5 = parse_csv('camion.csv', types=[str, int, str])
print(camion_5)

