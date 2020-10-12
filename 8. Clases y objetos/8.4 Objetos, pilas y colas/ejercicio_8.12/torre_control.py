# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:44:46 2020

@author: Claudio Collado

"""
#Clase provista en la teoria

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

        
    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


#Clase desarrollada para el ejercicio

class TorreDeControl():
    
    def __init__(self):
        '''Crea 2 colas, una para los arribos y otro para las partidas'''
        self.arribo = Cola() 
        self.partida = Cola()
        
    def nuevo_arribo(self,vuelo_llegada):
        '''
        Encola un vuelo que llegó y espera para aterrizar:
            *vuelo_llegada se ingresa como string
        Por cuestiones de seguridad se considera que los vuelos 
        que estan en el aire para aterrizar tienen prioridad 
        sobre los que estan esperando para despegar
        '''
        self.arribo.encolar(vuelo_llegada)
        
    def nueva_partida(self,vuelo_despegar):
        '''
        Encola un vuelo que espera para despegar:
            *vuelo_despegar se ingresa como string
       Una vez que ya no quedan vuelos esperando para 
       aterrizar desencola los que están esperando despegar
        '''
        self.partida.encolar(vuelo_despegar)
    
    
    def asignar_pista(self):
        '''Muestro un mensaje sobre la asignacion de pistas: Aterrizaje y despegue o 
           No hay vuelos en espera'''
        try:
            if len(torre.arribo.items) != 0:
                print('El vuelo ',self.arribo.desencolar(),' aterrizó con éxito')
            else:
                print('El vuelo ',self.partida.desencolar(),' despego con éxito')
        except:
            print('No hay vuelos en espera')
                 
    def ver_estado(self):
        
        a = [ 'Vuelos en aire esperando para aterrizar:' ]
        for obj in torre.arribo.items:
            s = object.__str__(obj)
            a.append(s)
        t = [ 'Vuelos en tierra esperando para despegar:' ]
        for obj in torre.partida.items:
            s = object.__str__(obj)
            t.append(s)
        print (' '.join(a) + '\n' + ' '.join(t))

#%%

#Ejecucion de las pruebas del enunciado

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()

