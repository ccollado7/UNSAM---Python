# -*- coding: utf-8 -*-

import random


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def es_33(mano):
    index_siete = []
    index_seis = []
    for carta in mano:
        if carta[0] == 7:
            index_siete.append(mano.index(carta))
        elif carta[0] == 6:
            index_seis.append(mano.index(carta))
    if len(index_seis)>0 and len(index_siete)>0:
        for indice_7 in index_siete:
            for indice_6 in index_seis:
                if mano[indice_7][1] == mano[indice_6][1]:
                    treintaytres = True
                else:
                    treintaytres = False
    else:
        treintaytres = False
        
    return treintaytres

def es_32(mano):
    if not(es_33(mano)):
        index_siete = []
        index_cinco = []
        for carta in mano:
            if carta[0] == 7:
                index_siete.append(mano.index(carta))
            elif carta[0] == 5:
                    index_cinco.append(mano.index(carta))
        if len(index_cinco)>0 and len(index_siete)>0:
            for indice_7 in index_siete:
                for indice_5 in index_cinco:
                    if mano[indice_7][1] == mano[indice_5][1]:
                        treintaydos = True
                    else:
                        treintaydos = False
        else:
            treintaydos = False
    else:
        treintaydos = False
        
    return treintaydos

def es_31(mano):
    if not(es_33(mano)) and not(es_32(mano)):
        index_cuatro = []
        index_cinco = []
        index_seis = []
        index_siete = []
        for carta in mano:
            if carta[0] == 7:
                index_siete.append(mano.index(carta))
            elif carta[0]==6:
                index_seis.append(mano.index(carta))
            elif carta[0] == 5:
                index_cinco.append(mano.index(carta))
            elif carta[0] == 4:
                index_cuatro.append(mano.index(carta))
        if len(index_cinco)>0 and len(index_seis)>0:
            for indice_6 in index_seis:
                for indice_5 in index_cinco:
                    if mano[indice_6][1] == mano[indice_5][1]:
                        treintayuno = True
                    else:
                        treintayuno = False
        elif len(index_cuatro)>0 and len(index_siete)>0:
            for indice_4 in index_cuatro:
                for indice_7 in index_siete:
                    if mano[indice_4][1] == mano[indice_7][1]:
                        treintayuno = True
                    else:
                        treintayuno = False
        else:
            treintayuno = False
    else:
        treintayuno = False
    
    return treintayuno


# 1 mano de cartas
mano = random.sample(naipes,3)
#mano = [(5, 'espada'), (6, 'copa'), (7, 'espada')]
#mano = [(11, 'espada'), (6, 'espada'), (7, 'espada')]
#mano = [(5, 'espada'), (4, 'espada'), (7, 'espada')]
treintaytres = es_33(mano)
treintaydos = es_32(mano)
treintayuno = es_31(mano)

print(f'La mano es {mano}')
if treintaytres:
    print('Para la mano obtenida hay 33 de envido')
elif treintaydos:
    print('Para la mano obtenida hay 32 de envido')
elif treintayuno:
    print('Para la mano obtenida hay 31 de envido')
else:
    print('En esta mano no hay 33, 32 ni 31 de envido')

#%%
#Experimento con múltiples manos

N = 100000
G33 = []
G32 = []
G31 = []

for r in range(10):
    for n in range(N):
        mano = random.sample(naipes,3)

    G33.append(sum([es_33(random.sample(naipes,3)) for i in range(N)]))
    G32.append(sum([es_32(random.sample(naipes,3)) for i in range(N)]))
    G31.append(sum([es_31(random.sample(naipes,3)) for i in range(N)]))
   

print(f'La probabilidad de sacar 33 de envido es {sum(G33)/(N*10)}')
print(f'La probabilidad de sacar 32 de envido es {sum(G32)/(N*10)}')
print(f'La probabilidad de sacar 31 de envido es {sum(G31)/(N*10)}')


'''
Out:
La probabilidad de sacar 33 de envido es 0.01476
La probabilidad de sacar 32 de envido es 0.0136
La probabilidad de sacar 31 de envido es 0.02705
'''