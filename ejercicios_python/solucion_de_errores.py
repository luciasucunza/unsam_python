#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario:    El error era semántico y estaba ubicado en la linea 'return False'.
#               Consitía en que la función solo analizaba el primer caracter.
#               Si es una 'a' es correcto que retorne inmediatamente, pero en caso de no serlo es necasario analizar los siguientes caracteres.

#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

for string in ['UNSAM 2020','abracadabra','La novela 1984 de George Orwell']:
    print('"',string, '" : ', tiene_a(string))
#%%
#Ejercicio 3.2. Función tiene_a()
#Comentario:    Los errores era de sintaxis:
#                     En las sentencias 'def', 'while' e 'if', faltaron los ':' al final
#                     En la comparación del 'if', la misma se escribe con '==' no '='
#                     En la linea 'return Falso', la expresión correcta del booleno es 'False' no 'Falso'

#    A continuación va el código corregido                
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

for string in ['UNSAM 2020','abracadabra','La novela 1984 de George Orwell']:
    print('"',string, '" : ', tiene_a(string))

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario:    El error es en tiempo de ejecución, la función está preparada para recibir strings, no enteros como en la linea 'tiene_uno(1984)'
#               Se puede corregir de dos formas, dependiendo de lo que realmente se quiere hacer:
#                    - Arrojar un mensaje de error y pedir un reingreso de datos
#                    - Convertir en string la entrada si la misma no es un string 

#    A continuación va el código corregido con el segundo criterio                
def tiene_uno(expresion):
    if type(expresion)!= str:
        expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

for string in ['UNSAM 2020','La novela 1984 de George Orwell', 1984]:
    print('"',string, '" : ', tiene_uno(string))

#%%
#Ejercicio 3.4. Función suma()
#Comentario:    El error es semánitco y se ubica en la definición de la función
#               La función no retorna ningun valor, es decir 'suma(a,b)' es igual a 'None' 

    #    A continuación va el código corregido                
def suma(a,b):
    return a + b
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario:    El error es semántico, cada vez que se append agrega el mismo objeto 'registro' 
#               En las primeras tres lineas luego del for lo que se hace es modificar el objeto registro ya existente, es decir, su contenido
#               la lista 'camion' lo que hace es adjuntar a registro varias veces, dando una lista de todos elementos iguales.
#               Una solución es hacer que registro apunte a distintos objetos y no modificar el contenido del mismo una y otra vez.
#               Al hacer esto la lista va a ser el conjunto de disintos objetos, ya que registro no siempre apunta a lo mismo
    #    A continuación va el código corregido 
from pprint import pprint
import csv

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {encabezado[0]:fila[0], encabezado[1]:int(fila[1]), encabezado[2]:float(fila[2])}
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
