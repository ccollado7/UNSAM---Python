

def propagar(lista):
    
    
   # largo= len(lista)
    
    listaprop=[]
    anterior=-1
    estado=0
    
    for i,elemento in enumerate(lista):
            
        if elemento==-1: #si esta apagado, queda igual en listaprop
            anterior=elemento
            estado=elemento
            listaprop.insert(i,estado)
           
        if elemento==0 and anterior==0: #si es 0 y antes era 0,no se prende
            anterior=elemento
            estado=elemento
            listaprop.insert(i,estado)
          
        if elemento==0 and anterior==1: #si es 0 y antes hubo un 1, se prende
            estado=1
            listaprop.insert(i,estado)
            anterior=1
       
        if elemento==0 and anterior==-1: #si es 0 y antes era -1,no se prende
            anterior=0
            estado=0
            listaprop.insert(i,estado)
            
        if elemento==1: #si es 1, queda prendido
            estado= 1
            anterior=1
            listaprop.insert(i,estado)
          
        i+=1 

#Ahora voy para la izquierda en listaprop. Tengo que invertir la lista
#que sale de la primera parte de la función
   
    prop_inv= listaprop[::-1] 
    listaprop2=[]
    anterior_izq=-1
    
#solo me interesa cambiar los estados alrededor de los 0 que tenian 1 al lado
    
    for j,elemento_izq in enumerate(prop_inv):
    
        if elemento_izq==1 or elemento_izq==-1:
            anterior_izq=elemento_izq
            estado_izq=elemento_izq
            listaprop2.insert(j,estado_izq)     
        
        if elemento_izq==0 and anterior_izq==0:
            anterior_izq=elemento_izq
            estado_izq=elemento_izq
            listaprop2.insert(j,estado_izq)
          
        if elemento_izq==0 and anterior_izq==1: #si es 0 y antes hubo un 1, se prende
            estado_izq=1
            listaprop2.insert(j,estado_izq)
            anterior_izq=1
       
        if elemento_izq==0 and anterior_izq==-1: #si es 0 y antes era -1,no se prende
            anterior_izq=elemento_izq
            estado_izq=elemento_izq
            listaprop2.insert(j,estado_izq)
            
        j+=1
        
    listapropfinal=listaprop2[::-1]    #esta lista estaba invertida, la vuelvo
                                       #a su estado original
        
        
    return(listapropfinal)
 
       
casa=propagar([0,1,0,0,1])
print(casa)
#output=[1,1,1,1,1]

casa=propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
print(casa)
#output [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]


#%%IDEA A FUTURO
# def propagar(lista):
#     for i in range(0, len(lista)-1):
#         if lista[i] == 1 and lista[i+1] == 0:
#             lista[i+1] = 1
#     for i in range (len(lista)-1, 0, -1):
#         if (lista[i] == 1) and (lista[i-1] == 0):
#             lista[i-1] = 1
#     return lista (editado) 

#%% Revision de Pares - Casos de prueba evaluados

# Caso 1: [1,0,0,0]
    #Resultado: [1, 1, 1, 1] (Correcto)
    
# Caso 2: [0,-1,0,0,1]
    #Resultado: [0, -1, 1, 1, 1] (Correcto)
    
# Caso 3: [0,-1,0,-1,1]
    #Resultado: [0,-1,0,-1,1] (Correcto)   
    
# Caso 4: [0 for x in range(10)]
    #Resultado: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] (Correcto)  

# Caso 5: [1 for x in range(100)]
    #Resultado: [1, 1, 1, 1, 1, 1, 1, ,1] (Correcto)  
    
# Caso 6: [(x%3)-1 for x in range(30)]
    #Resultado: [-1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1] (Correcto)

