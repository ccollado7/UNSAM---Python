#%%
import csv
from collections import Counter

#%%
# esta funcion recibe un parque y devuelve la info
# de todos los datos de los arboles de ese parque 
def leer_parque (nombre_archivo, parque):
    file = open (nombre_archivo, encoding= "utf8")
    rows = csv.reader(file)
    headers = next(rows)
    registro = []    
    for r in rows:
        arbol = {}
        arbol = dict(zip(headers, r))
        registro.append (arbol)

    li_par = []
    for i in registro:
        if i["espacio_ve"] == parque:
            arbol = {}
            arbol = i
            li_par.append (arbol)
    
    return li_par # debug: 690 arboles en GRAL PAZ
    file.close ()


#%%
# Esta funcion toma una lista de arboles generada por
# def leer_parque y devuelve el 
# conjunto de spp que figura en la lista
def especies (lista_arboles):
    contenedor = []
    for arbol in lista_arboles:
        contenedor.append (arbol["nombre_com"])
    spp = set (contenedor)
    return spp

# Esta funcion toma lista de arboles generada por 
# def leer_parque y devuelve un diccionario en que
# las especies son las claves y tengan como valores
# asociados la cantidad de ejemplares

#%%
def contar_ejemplares (lista_arboles):
    ejem = {}
    for arbol in lista_arboles:
        try:
            ejem[arbol["nombre_com"]] += 1
        except KeyError:
            ejem[arbol["nombre_com"]] = 1
    return (ejem)

#%%
# Combiná la función contar_ejemplares con leer_parque()
# y con el método most_common() para informar las cinco
# especies más frecuentes en cada uno de los siguientes parques:
# GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO

# GENERAL PAZ
gp = leer_parque ("arbolado-en-espacios-verdes.csv","GENERAL PAZ")
a = contar_ejemplares (gp)
b = Counter (a)
c = b.most_common (5)
print (f"Las 5 especies mas comunes del parque General Paz: {c}")
# SALIDA
# Las 5 especies mas comunes del parque General Paz: 
# [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49),
# ('Palo borracho rosado', 44), ('Fenix', 40)]

# ANDES, LOS
gp = leer_parque ("arbolado-en-espacios-verdes.csv","ANDES, LOS")
a = contar_ejemplares (gp)
b = Counter (a)
c = b.most_common (5)
print (f"Las 5 especies mas comunes del parque Los Andes: {c}")
# SALIDA
# Las 5 especies mas comunes del parque Los Andes:
# [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21),
# ('Palo borracho rosado', 18), ('Lapacho', 12)]

# CENTENARIO
gp = leer_parque ("arbolado-en-espacios-verdes.csv","CENTENARIO")
a = contar_ejemplares (gp)
b = Counter (a)
c = b.most_common (5)
print (f"Las 5 especies mas comunes del parque Centenario: {c}")
# SALIDA
# Las 5 especies mas comunes del parque Centenario: 
# [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42),
# ('Palo borracho rosado', 41), ('Fresno americano', 38)]

#%%


# Esta funcion recibe una lista de arboles de la funcion leer_parque
# y una especie, y devuelve una lista con las alturas de los ejemplares
# de esa especie en la lista

def obtener_alturas (lista_arboles, especie):
    altura = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            alt = float(arbol["altura_tot"])
            altura.append (alt)
    return (altura)

# GENERAL PAZ
gp = leer_parque ("arbolado-en-espacios-verdes.csv","GENERAL PAZ")
a = obtener_alturas (gp, "Jacarandá")
med = sum(a) / len(a)
print (f"El Jacarandá más alto del parque General Paz mide: {max(a):0.2f} y el promedio es {med:0.2f}")
# SALIDA
# El Jacarandá más alto del parque General Paz mide: 16.00 y el promedio es 10.20

# ANDES, LOS
gp = leer_parque ("arbolado-en-espacios-verdes.csv","ANDES, LOS")
a = obtener_alturas (gp, "Jacarandá")
med = sum(a) / len(a)
print (f"El Jacarandá más alto del parque Los Andes mide: {max(a):0.2f} y el promedio es {med:0.2f}")
# SALIDA
# El Jacarandá más alto del parque Los Andes mide: 25.00 y el promedio es 10.54

# CENTENARIO
gp = leer_parque ("arbolado-en-espacios-verdes.csv","CENTENARIO")
a = obtener_alturas (gp, "Jacarandá")
med = sum(a) / len(a)
print (f"El Jacarandá más alto del parque Centenario mide: {max(a):0.2f} y el promedio es {med:0.2f}")
# SALIDA
# El Jacarandá más alto del parque Centenario mide: 18.00 y el promedio es 8.96

#%%

# Esta función recibe una lista de arboles y una especie y
# devuelve una lista con las inclinaciones de los ejemplares

def obtener_inclinaciones (lista_arboles, especie):
    inclinacion = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inc = float(arbol["inclinacio"])
            inclinacion.append (inc)
    return (inclinacion)

#%%
# Esta funcion recibe una lista de arboles y devuelve la especie
# q tiene el ejemplar mas inclinado y su inclinacion

def especimen_mas_inclinado (lista_arboles):       
    arb = ""
    max = 0
    for arbol in lista_arboles:
        inc = float(arbol["inclinacio"])
        if inc > max:
            max = inc
            arb = arbol["nombre_com"]
    return (arb, max)

#%%
# Esta funcion recibe una lista de arboles, devuelve la
# especie que en promedio tiene la mayor inclinacion y el 
# promedio calculado

def especie_promedio_mas_inclinada (lista_arboles):
    d_esp = {}
    for arbol in lista_arboles:
        try:
            l = d_esp[arbol["nombre_com"]]
            l.append(float(arbol["inclinacio"]))
        except KeyError:
            l= []
            d_esp[arbol["nombre_com"]] = l
            l.append(float(arbol["inclinacio"]))            
    
    arb = ""
    max = 0
    for key in d_esp:
        prom = sum(d_esp[key]) / len(d_esp[key])
        if prom > max:
            max = prom
            arb = key

    return (arb, max)
