# comparaciones_ordenamiento.py

# Ejercicio 11.5 +11.7

#%%
import random

def generar_lista(N):
    ''' 
    Precondicion: N debe ser un entero positivo
        Devuelve: Una lista de N números aleatorios del 1 al 1000, con repeticion.
    '''
    lista = []
    for i in range(N):
        lista.append(random.randint(1, 1000))
    return lista


#%% Ordenamiento por selección
def ord_seleccion(lista):
    '''Ordena una lista de elementos según el método de selección.
       Precondicion: los elementos de la lista deben ser comparables.
           Devuelve: lista está ordenada.
                     un entero con la cantida de comparaciones'''
   
    comp = 0 #Cantidad de comparaciones
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        
        # cada vez que llamo a buscar_max hago b-a compraciones
        comp += n 

        # intercambiar el valor que está en p con el útlimo valor del segmento
        lista[p], lista[n] = lista[n], lista[p]

        n = n - 1
        
    return comp

def buscar_max(lista, a, b):
    ''' 
    Precondicion: Lista no vacía y con elementos comparables
                  a y b deben ser posciones del segmento (a<b)
        Devuelve: Posición del máximo elemento en el segmento de la lista
    '''
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:    
            pos_max = i
    return pos_max


#%% Ordenamiento por inserción
def ord_insercion(lista):
    '''Ordena una lista de elementos según el método de inserción.
       Precondicion: los elementos de la lista deben ser comparables.
           Devuelve: lista está ordenada.
                     un entero con la cantida de comparaciones'''
                     
    comp = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comp += 1                      #Sumo una comprarción       
            comp += reubicar(lista, i + 1) #Sumo las comparaciones de reubicar
    
    return comp

def reubicar(lista, p):
    ''' 
    Precondicion: Lista no vacía y con elementos comparables
                  p deben ser posciones de la lista
        Devuelve: Lista con el elemeto de la posición p ubicado detro del 
                  segmento [0:p-1]
    '''

    comp = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        comp +=1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    comp +=1
    lista[j] = v
    
    return comp


#%% Ejemplo 11.2 Burbujeo   
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbuja.
       Precondicion: los elementos de la lista deben ser comparables.
           Devuelve: lista está ordenada.
                     un entero con la cantida de comparaciones
    '''

    comp = 0 #Cantidad de comparaciones
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        
        #burbujear la lista hasta la posición n
        burbujear(lista, 0, n)
    
        # cada vez que llamo a burbujear hago b-a compraciones
        comp += n 
        
        n = n-1
        
    return comp
        
def burbujear(lista, a, b):
    '''Burbujea un segmento de la lista de elementos.
       Precondición: Lista no vacía y con elementos comparables
                     a y b deben ser posciones del segmento (a<b)
           Devuelve: la lista con el mayor valor del segmento en la posición b.
    '''
       
    for i in range(a, b):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            
            
#%% Ordenamiento divide y triunfaras
def merge_sort(lista):    
    '''Ordena lista mediante el método merge sort.
       Precondicion: lista debe contener elementos comparables.
           Devuelve: una nueva lista ordenada.
                     un entero con la cantidad de comparaciones
    '''
    comps = 0
    
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comps_i = merge_sort(lista[:medio])
        der, comps_d = merge_sort(lista[medio:])
        lista_nueva, comps_merg = merge(izq, der)
        comps = comps_i + comps_d + comps_merg
    return lista_nueva, comps

 
def merge(lista1, lista2):
    '''Intercala los elementos de lista1 y lista2 de forma ordenada.
       Precondicion: lista1 y lista2 deben estar ordenadas.
           Devuelve: una lista con los elementos de lista1 y lista2
                     un entero con la cantidad de comparaciones
    '''
    comps = 0
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comps += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comps           
            
            
#%% Experimento
import matplotlib.pyplot as plt    
        
comparaciones_seleccion = []
comparaciones_insercion = []
comparaciones_burbujeo = []
comparaciones_mergesort = []
          
for i in range(1, 256+1):
    lista = generar_lista(i)
    l_sel = lista.copy()
    l_ins = lista.copy()
    l_bur = lista.copy()
    comparaciones_seleccion.append(ord_seleccion(l_sel))
    comparaciones_insercion.append(ord_insercion(l_ins))
    comparaciones_burbujeo.append(ord_burbujeo(l_bur))
    l_mer, aux_comp = merge_sort(lista)
    comparaciones_mergesort.append(aux_comp)
    # PRINTS PARA DEBUGEAR
    # print(i,'Lista Original:', lista)
    # print('Lista Ordenada por Selección:', l_sel, '  (', comparaciones_seleccion[i], ')')
    # print('Lista Ordenada por Inserción:', l_ins, '  (', comparaciones_insercion[i], ')')
    # print('Lista Ordenada por Burbujeo: ', l_bur, '  (', comparaciones_burbujeo[i], ')')
    # print('Lista Ordenada por MergeSort:', l_mer, '  (', aux_comp, ')')

plt.figure(1)
plt.title('Cantidad de comparaciones por método de ordenamiento')
plt.plot(comparaciones_seleccion, '.r', label='Selección')
plt.plot(comparaciones_insercion, 'g', label='Inserción')
plt.plot(comparaciones_burbujeo, 'b', label='Burbujeo')
plt.plot(comparaciones_mergesort, 'y', label='MergeSort')
plt.legend()
plt.xlabel('Longitud de la lista')
plt.ylabel('Cantidad de comparciones')
plt.show()


'''En la gráfica podemos observar como se cumple que la cantidad de 
comparaciones del ordenamiento por burbujeo y por selección es N^2.
Además se observa la baja cantidad de comparaciones del método MergeSort'''