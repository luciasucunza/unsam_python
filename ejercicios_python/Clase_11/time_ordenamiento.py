# time_ordenamiento.py
    
import timeit as tt
import numpy as np
import random
import matplotlib.pyplot as plt

#%%
def experimento_timeit_orden(listas, num, tipo):
    '''Realiza un experimento usando timeit para evaluar métodos de ordenamiento.
    Precondicion: 'listas' debe ser una lista de listas.
                  'num' indica la cantidad de repeticiones a ejecutar.
                  'tipo' indica el tiempo de ordenamiento a experimetar
        Devuelve: Un vector con los tiempos de ejecución de cada lista.
    '''
    
    tiempos_orden = []
    
    global lista
    
    # evalúo el método de ordenamiento correspondiente para cada lista
    if tipo == 'Seleccion':
        for lista in listas:
            tiempo_sel = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
            tiempos_orden.append(tiempo_sel)
    elif tipo == 'Inserción':
        for lista in listas:
            tiempo_ins = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
            tiempos_orden.append(tiempo_ins)
    elif tipo == 'Burbujeo':
        for lista in listas:
            tiempo_bur = tt.timeit('ord_burbujeo(lista.copy())', number = num, globals = globals())
            tiempos_orden.append(tiempo_bur)
    elif tipo == 'MargeSort':
        for lista in listas:
            tiempo_mar = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
            tiempos_orden.append(tiempo_mar)            
            
    # paso los tiempos a arrays
    tiempos_orden = np.array(tiempos_orden)
    
    return tiempos_orden


#%%
def generar_lista(N):
    ''' 
    Precondicion: N debe ser un entero positivo
        Devuelve: Una lista de N números aleatorios del 1 al 1000, con repeticion.
    '''
    lista = []
    for i in range(N):
        lista.append(random.randint(1, 1000))
    return lista

def generar_listas(Nmax):
    '''
    Precondicion: N debe ser un entero positivo
        Devuelve: Una lista de listas, una de cada longitud entre 1 y Nmax, de
                  números aleatorios del 1 al 1000, con repeticiones
    '''
    listas = []
    for n in range(1, Nmax):
        listas.append(generar_lista(n))
    return listas


#%% Ordenamiento por selección
def ord_seleccion(lista):
    '''Ordena una lista de elementos según el método de selección.
       Precondicion: los elementos de la lista deben ser comparables.
           Devuelve: lista está ordenada.
    '''
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el útlimo valor del segmento
        lista[p], lista[n] = lista[n], lista[p]

        n = n - 1

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
    '''
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1) 

def reubicar(lista, p):
    ''' 
    Precondicion: Lista no vacía y con elementos comparables
                  p deben ser posciones de la lista
        Devuelve: Lista con el elemeto de la posición p ubicado detro del 
                  segmento [0:p-1]
    '''
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


#%% Ejemplo 11.2 Burbujeo   
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbuja.
       Precondicion: los elementos de la lista deben ser comparables.
           Devuelve: lista está ordenada.
    '''
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        
        #burbujear la lista hasta la posición n
        burbujear(lista, 0, n)
    
        n = n-1
        
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
    '''
    
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva
 
def merge(lista1, lista2):
    '''Intercala los elementos de lista1 y lista2 de forma ordenada.
       Precondicion: lista1 y lista2 deben estar ordenadas.
           Devuelve: una lista con los elementos de lista1 y lista2
    '''
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


#%%
# Generamos las listas para realizar el experimento
listas = generar_listas(Nmax=256)
  
# Cantidad de repeticiones (OJO con no matar a la compu)
n = 15
  
# Realizamos el experimento
tiempos_seleccion = experimento_timeit_orden(listas, n, 'Seleccion')
tiempos_insersion = experimento_timeit_orden(listas, n, 'Inserción')
tiempos_burbujeo  = experimento_timeit_orden(listas, n, 'Burbujeo')
tiempos_margesort = experimento_timeit_orden(listas, n, 'MargeSort')

# Ploteamos los resultados
plt.figure(1)
plt.title('Tiempo de ejecución por método de ordenamiento')
plt.plot(tiempos_seleccion, 'r', label='Selección')
plt.plot(tiempos_insersion, 'g', label='Inserción')
plt.plot(tiempos_burbujeo, 'b', label='Burbujeo')
plt.plot(tiempos_margesort, 'y', label='MergeSort')
plt.legend()
plt.xlabel('Longitud de la lista')
plt.ylabel('Tiempo de ejecución')
plt.show()
                  