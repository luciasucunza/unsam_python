#torre_de_control.py

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

    def __repr__(self):
        return f'{self.items}'

class TorreDeControl(Cola):
    '''Representa el manejo de una torre de control para el arrivo y despegue de aviones.'''
    
    def __init__(self):
    
        self.arribos = Cola()
        self.partidas = Cola()      
            
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)        
    
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)        
    
    def ver_estado(self):
    
        print(f'Vuelos esperando para aterrizar: {self.arribos}')
        print(f'Vuelos esperando para despegar: {self.partidas}')        
        
    def asignar_pista(self):
        '''Asigna una pista para aterrizaje, si no hay vuelos de arribos, asigna pista para despegue'''
        if self.arribos.esta_vacia():

            if not self.partidas.esta_vacia():

                vuelo = self.partidas.desencolar()
                print(f'El vuelo {vuelo} despegó con éxito')
            
            else:
                print('No hay vuelos en espera')
        else:
            
            vuelo = self.arribos.desencolar()
            print(f'El vuelo {vuelo} aterrizó con éxito')
            

torre = TorreDeControl()

torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')

torre.ver_estado()
#Vuelos esperando para aterrizar: AR156, AR32
#Vuelos esperando para despegar: KLM1267

torre.asignar_pista()
#El vuelo AR156 aterrizó con éxito.

torre.asignar_pista()
#El vuelo AR32 aterrizó con éxito.

torre.asignar_pista()
#El vuelo KLM1267 despegó con éxito.

torre.asignar_pista()
#No hay vuelos en espera.