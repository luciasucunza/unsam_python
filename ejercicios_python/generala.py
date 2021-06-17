import random 
'''
Para ver que funcione correctamente descomentar los prints y colocar un N menor, por ejemplo de 10

Para que los cometarios del funcionamiento resalten por sobre los prints comentados
'''

def tirar (n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1, 6))
    return tirada

def tirada_generala():
    '''Realiza de 1 a 3 tiradas, devuelve True si saca generala y False si no'''''
    tirada = tirar(5)
    #print('---------------------')
    #print('Tirada 1:', tirada)
    
    '''Me fijo en esta primera tirada la máxima cantidad de repeticiones, si es 5 quiere decir que es generala'''
    cantidades = [0,0,0,0,0,0]
    for i in tirada:
        cantidades[i-1] +=1        
    num_iguales = max(cantidades)    
    if num_iguales == 5:
        return True
    
    '''
    Como no hubo generala vuelvo a tirar los dados, aquellos que no pertenecen al grupo de mayor cantidad de repeticiones
    Si dos o más numeros se repiten la misma cantidad de veces se toma elige seguir con el valor menor (esto se debe a que la funcion index devuelve la priemra ocurrencia)
    '''
    tirada =  [cantidades.index(num_iguales)+1 for x in range(num_iguales)] + tirar(5-num_iguales)
    #print('Tirada 2:', tirada)
    
    '''
    #Me fijo en esta segunda tirada la máxima cantidad de repeticiones, si es 5 quiere decir que es generala
    '''
    
    cantidades = [0,0,0,0,0,0]
    for i in tirada:
        cantidades[i-1] +=1        
    num_iguales = max(cantidades)    
    if num_iguales == 5:
        return True
       
    '''    
    #Como no hubo generala vuelvo a tirar los dados, aquellos que no pertenecen al grupo de mayor cantidad de repeticiones
    #Si dos o más numeros se repiten la misma cantidad de veces se toma elige seguir con el valor menor (esto se debe a que la funcion index devuelve la priemra ocurrencia)
    '''
    tirada =  [cantidades.index(num_iguales)+1 for x in range(num_iguales)] + tirar(5-num_iguales)
    #print('Tirada 3:', tirada)
    
    '''
    #Me fijo en esta última si es generala
    '''
    for i in range(1,len(tirada)):
        if tirada[i] != tirada[0]:
            return False
    return True


N = 100000
G = sum([tirada_generala() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala en una ronda de tres tiros.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')