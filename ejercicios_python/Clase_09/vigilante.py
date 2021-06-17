# vigilante.py
''' Incluye dos ejercicios: 9.6 y 9.7
Para correr uno se debe comentar el bloque correspondiente al otro ejercicio.
'''

import os
import time

#%%
def vigilar(filename):
    with open('Data/mercadolog.csv') as f:
        f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
        
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.5)   # Esperar un rato y
                continue          # vuelve al comienzo del while
            
            yield line


#%%
''' Ejercicio 9.6: Uso de un generador para producir datos
Programa que abra el archivo 'Data/mercadolog.csv', va al final, y espere 
nuevos datos
'''

# if __name__ == '__main__':
#     for line in vigilar('Data/mercadolog.csv'):
#         fields = line.split(',')
#         nombre = fields[0].strip('"')
#         precio = float(fields[1])
#         volumen = int(fields[2])
#         if volumen > 1000:
#             print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
            
            
#%%
'''Ejercicio 9.7: Cambios de precio de un camión
Programa que informa las líneas que tienen precios de lotes incluídos en un 
camión, e ignora el resto de los productos
'''

if __name__ == '__main__':
    import informe 
    camion = informe.leer_camion('Data/camion.csv')
    
    for line in vigilar('Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')