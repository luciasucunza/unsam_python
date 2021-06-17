# 10_Ejemplos.py


#%%
'''Ejemplo función recursiva factorial, dos versiones'''

def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    if n == 1:
        return 1
    return n * factorial(n - 1)

def factorial1(n):
    if n == 1:
        r = 1
        return r

    f = factorial1(n-1)
    r = n * f
    return r
#%%
'''Ejemplo función iterativa factorial'''

def factorial2(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact

#%%
'''Ejemplo función recursiva potencia'''

def _potencia(b, n):
    """Precondición: n entero positivo
       Devuelve: b**n"""
    if n == 0:
        return 1
    
    if n % 2 == 0:
        p = _potencia(b, n//2) 
        return p*p
    else:
        p = _potencia(b, (n-1)//2) 
        return p*p*b
#%%
'''Ejemplo función iterativa potencia'''

def potencia2(b, n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2

    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b

    return p

#%%
'''Ejemplo función recursiva Fibonacci'''

def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)
    return res
#%%
'''Ejemplo función iterativa Fibonacci'''

def fib2(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn

#%%
'''Ejemplo función recursiva suma, dos versiones'''

def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:])
   return res

def sumar2(lista, suma = 0): #Recursión de cola
    """Devuelve la suma de los elementos en la lista."""
    res = suma
    if len(lista) != 0:
        res = sumar2(lista[1:], lista[0] + suma)
    return res

#%%
'''Ejemplo función iterativa suma, a partir de la recursión de cola'''

def sumar3(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma
        
#%%
'''Ejemplo función recursiva promedio, sin cambiar la firma de la función'''

def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):       #Se define dentro para que no sea visible
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

#%%
'''Ejemplo función recursiva potencia, con envoltorio para parámetros'''

def potencia(b, n):
    """Precondición: n es entero
       Devuelve: b^n."""
    if n < 0:
        b = 1 / b
        n = -n
    return _potencia(b, n)