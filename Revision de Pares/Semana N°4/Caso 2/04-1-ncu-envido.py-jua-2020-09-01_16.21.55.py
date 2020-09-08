#envido.py
#calulos para la proba de envido
#importamos las librerias
import random
#primero armamos el mazo 
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['o', 'c', 'e', 'b']
naipes = [(valor,palo) for valor in valores for palo in palos]
#print(random.sample(naipes,k=3))

def envido(lis) :
    'esta funcion nos dice si tenemos envido o no'
    # la variable resultado es env
    env=0
    # como la combinaciones para analizar no son tantas lo hacemos de a pares
    # par 1 2
    if lis[0][1]==lis[1][1] and lis[0][0] < 10 and lis[1][0] <10 :
        env=1
    # par 2 3
    if lis[0][1]==lis[2][1] and lis[0][0] < 10 and lis[2][0] <10 :
        env=1
    # par 1 3
    if lis[1][1]==lis[2][1] and lis[1][0] < 10 and lis[2][0] <10 :
        env=1
    return env
mano=random.sample(naipes,k=3)
print(mano)
print(envido(mano))

def proba_envido(nintentos):
    i=0 #cantidad de intentos
    env=0
    while i < nintentos :
        i+=1
        mano=random.sample(naipes,k=3)
        env+=envido(mano)
    
    proba=env/nintentos*100
    print(f'la proba de envido en {nintentos} intentos es {proba:0.2f}%')

proba_envido(100000)