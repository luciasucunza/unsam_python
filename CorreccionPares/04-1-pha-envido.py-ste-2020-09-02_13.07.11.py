#envido.py
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def envido():
    mano=random.sample(naipes,k=3)
    #hago un dict con los palos y los valores
    mano_ordenada={}
    for x, y in mano:
        if y in mano_ordenada:
            mano_ordenada[y].append(x)
        else:
            mano_ordenada[y]=[x] 
    
    for palo in palos:
        if palo in mano_ordenada:
            if len(mano_ordenada[palo])>=2:   #hay envido
                mano_ordenada[palo].sort(reverse=True) #ordeno de mayor a menor
                for m in mano_ordenada[palo]:
                    if m in [10,11,12]:
                        mano_ordenada[palo].append(m) #lo pongo al final de la lista
                        mano_ordenada[palo].remove(m) #lo saco del principio de la lista
                #sumo los dos primeros con valor mas alto de envido        
                valor=20  
                for i in range(2):
                    if mano_ordenada[palo][i] in [10,11,12]:
                        valor += 0
                    else:
                        valor+= mano_ordenada[palo][i]
               # print(f'Envido: {valor} de {palo}') 
            else: #no hay envido
                valor=0
                pass
    return valor
#%%
#Probabilidades de obtener envidos de 31,32 y 33 
N=1000000
env31=0
env32=0
env33=0
for i in range(N):
    env=envido()
    if env==31:
        env31+=1
    elif env==32:
        env32+=1
    elif env==33:
        env33+=1
prob31=env31/N
prob32=env32/N
prob33=env33/N
print(f'probabilidades para obtener envidos de 31: {prob31}, 32:{prob32} y 33:{prob33}')
