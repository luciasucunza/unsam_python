#busqueda_en_listas.py

#%%
def busqueda_lineal(lista, e):
    '''Devuleve la posición de la primera aparición del elemento en la lista, 
    si el elemento no está en la lista devuelve -1 '''
    pos = -1  
    for i, z in enumerate(lista):
        if z == e:
            pos = i  
            break    
    return pos
# busqueda_lineal([1, 4, 54, 3, 0, -1], 44)
# busqueda_lineal([1, 4, 54, 3, 0, -1], 3)
# busqueda_lineal([1, 4, 54, 3, 0, -1], 0)
# busqueda_lineal([], 42)

#%%
def buscar_u_elemento(lista, e):
    '''Devuleve la posición de la última aparición del elemento en la lista, 
    si el elemento no está en la lista devuelve -1 '''
    pos = -1
    for i, z in enumerate(reversed(lista),  1):
        if z == e:
            pos = len(lista)-i
            break
    return pos
# buscar_u_elemento([1,2,3,2,3,4],1)
# buscar_u_elemento([1,2,3,2,3,4],2)
# buscar_u_elemento([1,2,3,2,3,4],3)
# buscar_u_elemento([1,2,3,2,3,4],5)
    
#%%
def buscar_n_elemento(lista, e):
    '''Devuleve la cantidad de veces que un elemento está en la lista '''
    cont = 0
    for z in lista:
        if z == e:
            cont +=1
    return cont
# buscar_n_elemento(['1','2','3','4','1','2','3','4'], '3')
# buscar_n_elemento([0,1,2,3,2,2], 2)
# buscar_u_elemento([1,2,3,2,3,4],5)
    
#%%
def maximo(lista):
    '''Devuleve el máximo de una lista, 
    la lista debe ser no vacia y de números positivos'''
    m = lista[0]
    for e in lista:
        if e > m:
            m = e
    return m
# maximo([1,2,7,2,3,4])
# maximo([1,2,3,4])
# maximo([-5,4])
# maximo([-5,-4])
            
#%%
def minimo(lista):
    '''Devuleve el minimo de una lista, 
    la lista debe ser no vacia y de números positivos'''
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m
# minimo([1,2,7,2,3,4])
# minimo([4,3,2,1])
# minimo([-5,4])
# minimo([-5,-6])
