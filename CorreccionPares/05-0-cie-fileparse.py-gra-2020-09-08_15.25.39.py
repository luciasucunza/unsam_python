
# fileparse.py
import csv

def parse_csv(nombre_archivo, has_headers = True, select = None, types = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar que el archivo no tenga encabezado asignando False al parámetro has_headers.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select,
    que debe ser una lista de nombres de las columnas a considerar en el caso de que has_headers = True,
    o una lista de los índices de las columnas en el caso de que has_headers = False.
    Se puede cambiar el tipo de variable de las columnas determinando el parámetro types, que debe
    ser una lista con las funciones de conversión en el orden de las columnas
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if has_headers: # Si tiene encabezados hago un diccionario

            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
                
        else: #Si no tiene encabezados
            if select:
                indices = select
            else:
                indices = []
                
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
            # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                #Armo las tuplas
                registro = tuple(fila)
                registros.append(registro)
                
    return registros

camion = parse_csv('Data/camion.csv', types=[str, int, float])
cajones_lote = parse_csv('Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)