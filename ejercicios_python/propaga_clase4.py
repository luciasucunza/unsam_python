def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])

'''
1)¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no causan un IndexError en los bordes de la lista?
    Porque en el if antes de hacer ese indexado está la pregunta del rango de i
2)¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas perfectamente simétricas, no generan la misma cantidad de repeticiones de llamadas a la función propagar_al_vecino?
    Porque en el primer caso hasta llegar al 1 ningun vecino está encendido, recien cuando llega al anteúltimo se propaga el fuego una vez. En cambio en el segundo caso el fuego se comienza a propagar desde el primero, entonces simper el veicino está encendido
3.1)¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n?
    El ciclo puede repetirse n-1 veces, el peor caso ocurre cuando el ulitmo está encedido y todo el resto no.
3.2)¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n?
    Propagar vecino hace una cantidad de operaciones lineales, es decir recorre la lista una única vez y por cada elemento hace cierta cantidad de operaciones finitas, entonces podemos decir que n
3.3)Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar en una lista de largo n? ¿Es un algoritmo de complejidad lineal o cuadrática?
    En el peor caso y despreciando las constantes, se hacen n**2  operaciones, es decir que es cuadrática
'''

#%%
def propagar_a_derecha(l):
    n = len(l)
    m = l.copy()
    for i,e in enumerate(m):
        if e==1 and i<n-1:
            if m[i+1]==0:
                m[i+1] = 1
    return m
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld = propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

'''
1)¿Por qué se modificó la lista original?
    Porque las operaciones de la funcion "propagar_a_derecha" se hacen sobre la lista original
2)¿Por qué no quedó igual al estado propagado?
    Porque laen la fución "propagar_a_izquierda" al ordenar y desordenar crea otra lista (?) RARO
3)Corregí el código para que no cambie la lista de entrada.
4)¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n?
    Como máximo hace n operaciones, ya que recorre toda la lista (en realidad es n*3+2, pero las constantes se desprecian)
5)Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo propagar en una lista de largo n?
    Hace 2*n operaciones, ya que recorre la lista de adelante para atras y de atras para adelante
'''

#%%
def trad2s(l):
    '''traduce una lista con 1,0 y -1 a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x' a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

'''
1)¿Porqué se acorta la lista?
    Porque al separar por -1 la cadena estos valores no los manitene 
2)¿Podés corregir el error agregando un solo caracter al código?
    En la linea 96 ("ps=''.join(PW)"), se agrgó la 'x' para unir los elementos con un fosforo carbonizado
3)¿Te parece que este algoritmo es cuadrático como el Ejercicio 4.3 o lineal como el Ejercicio 4.4?
    Pienso que es lineal, la lista se recorre al menos dos veces entera, cuando se hacen las traducciones, luego una tercera vez para dividir por -1 y una última, pero por partes, para saber que fragmentos quemar
    Es decir que es lineal (n*4)
'''