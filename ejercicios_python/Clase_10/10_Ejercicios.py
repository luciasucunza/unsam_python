# 10_Ejercicios.py

#%% Ejemplo 10.1 Factorial
def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

#%% Ejemplo 10.2 Numeros Triangulares
def num_triangular(n):
    ''' 
    Precondición: n debe ser entero mayor a 0
        Devuelve: un entenro con el n-esimo número triangular
    '''
    if n == 1:
        return 1
    return n**2 - num_triangular(n-1)

#%% Ejemplo 10.3 Dígitos
def cant_digitos(n):
    ''' 
    Precondición: n debe ser entero positivo
    Devuelve: un entenro con la cantidad de digitos del numero n
    '''
    cant = 1
    if n//10 != 0:
        cant = cant + cant_digitos(n//10)
        
    return cant
    
#%% Ejemplo 10.4 Potencias
def es_potencia(b, n):
    ''' 
    Precondición: b y n deben ser enteros
        Devuelve: True si n es potencia de b, si no False
    '''
    
    def _es_potencia(b,n):
        if b%n != 0:
            return False
        else:
            if b == n:
                return True
            else:
                return _es_potencia(b/n, n)
    if b == 1:
        return True
    else:   
        return _es_potencia(b,n)
            
#%% Ejemplo 10.5 Subcadenas
def posiciones_de(a, b):
    ''' 
    Precondición: a y b deben ser cadenas
        Devuelve: lista de posiciones en donde se encuentra b en a
    '''
    indices = []
    if len(a) < len(b):
        return indices
    
    if a.endswith(b):
        indices.append( len(a)-len(b) ) 
        indices = indices + posiciones_de(a[:-len(b)], b)
    else:
        indices = indices + posiciones_de(a[:-1], b)
                   
    indices.sort()      
    return indices
    
# posiciones_de('Un tete a tete con Tete', 'te') -> [3, 5, 10, 12, 21]
# posicion_de('Hola, el koala esta en el ala de la lata', 'la') -> [2, 12, 27, 33, 36]
    
#%% Ejemplo 10.6 Paridad
    # 1 es impar
    # Un número mayor que 1 es impar si su antecesor es par
def par(n):
    '''
    Precondición: n debe ser un número natural
        Devuelve: True si el número es par, False si no es par
    '''    
    if n == 1:
        return False
    
    return impar(n-1)

def impar(n):
    '''
    Precondición: n debe ser un número natural
        Devuelve: True si el número es impar, False si no es impar
    '''
    if n == 1:
        return True
    
    return par(n-1)
    

#%% Ejemplo 10.7 Máximo
    # Sin usar Max()
def maximo(numeros):
    '''
    Precondición: numeros debe ser una lista, no vacia, de numeros reales
        Devuelve: El valor máximo dentro de la lista
    '''
    
    if len(numeros) == 1:
        return numeros[0]
    
    m = maximo(numeros[:-1])      #Para no llamar dos veces a la función si sale por else
    if numeros[-1] >= m:
        return numeros[-1]
    else:
        return m
    
#%% Ejemplo 10.8 Replicar
def replicar(lista, n):
    '''
    Precondición: n debe ser un entero mayor a 0
        Devuelve: El valor máximo dentro de la lista
    '''
    if n == 1:
        return lista
    
    
#%% Ejemplo 10.9 Pascal
def pascal(n, k):
    '''
    Precondición: n y k deben ser enteros positivos, k menor a n para estar dentro del triangulo
        Devuelve: El número en el triangulo de pascal alojado en fila n, columna k
    '''
    if k == 0 or k == n:
        return 1
    
    return pascal(n-1, k-1) + pascal(n-1, k)  

#%% Ejemplo 10.10 Combinatorios
def combinaciones(caracteres, k):
    '''
    Precondición: caracteres debe ser una lista de caracteres únicos
                  k debe ser un numero natural
        Devuelve: Imprime todas las combinaciones de elementos de longitud k
                  Envoltorio para no imprimr en cada paso
    '''
    
    
    def _combinaciones(caracteres, k):
        '''
        Precondición: caracteres debe ser una lista de caracteres únicos
                      k debe ser un numero natural
            Devuelve: Lista con todas las combinaciones de elementos de longitud k
        '''        
        if k == 1:
            return caracteres
        
        combinacion_parcial = _combinaciones(caracteres, k-1)
        combinacion_total = [ i+j for i in combinacion_parcial for j in caracteres]

        return combinacion_total    
    
    l = _combinaciones(caracteres,k)
    print(' '.join(l))

#%% Ejemplo 10.11 Búsqueda binaria
def bbinaria_rec(lista, e):
    '''
    Precondición: la lista debe estar ordenada de mayor a menor
        Devuelve: True si el elemento está en la lista, False si no está.
    '''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif e < lista[medio]:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[-medio:], e)
            
    return res

#%% Ejemplo 10.12 Envolviendo a Fibonacci
def fibonacci(n):
    '''
    Precondición: n debe ser un número entero positivo
        Devuelve: el n-ésimo número de Fibonacci, donde F(0)=0 y F(1)=1
    '''
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva utilizando 
        un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            Fn2, dict_fibo = fibonacci_aux(n-2, dict_fibo)
            Fn1, dict_fibo = fibonacci_aux(n-1, dict_fibo)
            F = Fn1 + Fn2 
            dict_fibo[n] = F
            
        return F, dict_fibo
    
    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F     

#%% Ejemplo 10.13 Hojas ISO y recursión
def hoja_ISO(n):
    '''
    Precondición: n debe ser un número entero mayor a 0
        Devuelve: el ancho y el largo de la hoja A(N) en milimetros
    '''
    
    if n == 0:
        ancho = 841
        largo = 1189
        
    else:
        pre_ancho, pre_largo = hoja_ISO(n-1)
        if pre_ancho > pre_largo:
            largo = pre_ancho//2
            ancho = pre_largo
        else:
            largo = pre_ancho
            ancho = pre_largo//2
        
    return ancho, largo