# torre_control.py
'''
BLOQUES:
    Definicion clase Cola
    Definicion clase TorreDeControl
    Pruebas de funcionamiento clase TorreDeControl y Cola
    Definicion clase Cola
    Pruebas de funcionamiento clase Pila
'''

#%%
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

#%%
class TorreDeControl:
    ''' Representa una torre de control de un aeropuerto
    Deben asignarse pistas a arribos y partidas, con máxima prioridad para los
    arribos.
    '''
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()
        
    def nuevo_arribo(self, nombre):
        self.arribos.encolar(nombre)
        
    def nueva_partida(self, nombre):
        self.partidas.encolar(nombre)
        
    def ver_estado(self):
        print('Vuelos esperando para aterrizar:', ', '.join(self.arribos.items))
        print('Vuelos esperando para despegar:', ', '.join(self.partidas.items))
        
    def asignar_pista(self):
        if not self.arribos.esta_vacia():
            print( 'El vuelo', self.arribos.desencolar(), 'aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            print( 'El vuelo', self.partidas.desencolar(), 'despegó con éxito.')
        else:
            print('No hay vuelos en espera.')
            
            
#%%
''' 
Si se corre todo el bloque imprime:
    Vuelos esperando para aterrizar: AR156, AR32
    Vuelos esperando para despegar: KLM1267
    El vuelo AR156 aterrizó con éxito.
    El vuelo AR32 aterrizó con éxito.
    El vuelo KLM1267 despegó con éxito.
    No hay vuelos en espera.  
'''         

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()          

#%%
class Pila:
    def __init__(self):
        '''Crea una pila vacia.'''
        self.items = []
        
    def apilar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)
        
    def desapilar(self):
        '''Elimina el útlimo elemento de la pila  y devuelve su valor. 
        Si la pila esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(len(self.items)-1)
        
    def esta_vacia(self):
        '''Devuelve True si la cola esta vacia, 
                    False si no.'''
        return len(self.items) == 0
        
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")
    
#%%
''' 
Si se corre todo el bloque imprime:
    Ejecutando g(), x vale 10
    Ejecutando f(), x vale 50
    Ejecutando g(), x vale 10
'''    
    
pila_de_llamadas = Pila()

#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)            

#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)

#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)           

#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado) 