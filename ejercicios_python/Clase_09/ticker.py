# ticker.py
''' Incluye dos ejercicios: 9.10, 9.11 y 9.12

Para correr uno se debe comentar el bloque con al función "if __name__()"
correspondiente a los otros ejercicios.


IMPORTANTE:
    
    Para correr el ejercicio 9.12 debe tener el ejercicio 
formato_tabla.py funcionando correctamente, y en el mismo directorio

'''

from vigilante import vigilar
import csv

#%%
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[i] for i in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows
            
def ticker(camion_file, log_file, fmt):
    import informe
    import formato_tabla
    
    camion = informe.leer_camion('Data/camion.csv')
    rows = parsear_datos(vigilar('Data/mercadolog.csv'))
    rows = (row for row in rows if row['nombre'] in camion)
    
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    
    for row in rows:
        precio = row['precio']
        rowdata = [ row['nombre'], f'{precio:0.2f}', str(row['volumen'])]
        formateador.fila(rowdata)
    
    
#%%
''' Ejercicio 9.10: Un pipeline más largo
Programa que elije algunas columnas específicas, los datos son diccionarios
'''

# if __name__ == '__main__':
#     lines = vigilar('Data/mercadolog.csv')
#     rows = parsear_datos(lines)
#     for row in rows:
#         print(row)


#%%
''' Ejercicio 9.11: Filtremos los datos
Programa que deja pasar únicamente aquéllos lotes incluídos en el camión
'''

# if __name__ == '__main__':
#     import informe
#     camion = informe.leer_camion('Data/camion.csv')
#     rows = parsear_datos(vigilar('Data/mercadolog.csv'))
#     rows = (row for row in rows if row['nombre'] in camion)
#     for row in rows:
#         print(row)

#%%
''' Ejercicio 9.12: El pipeline ensamblado
'''

if __name__ == '__main__':
    ticker('Data/camion.csv', 'Data/mercadolog.csv', 'txt')
    # ticker('Data/camion.csv', 'Data/mercadolog.csv', 'csv')
