# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types= None, has_headers= True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        registros = []

        # Lee los encabezados del archivo
        if has_headers: #Si tiene encabezado
            encabezados = next(filas)
        
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Determinar el tipo de objeto    
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else: #Si especificamos en has_headers= False que no tiene encabezado
            for fila in filas:
                if not fila:
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]    
                # Armar el diccionario
                registro = tuple(fila)
                registros.append(registro)
    return registros

# Testeo
# camion = parse_csv('Data/camion.csv', select = ['precio', 'nombre'], types = [float,str])
# precios = parse_csv('Data/precios.csv', types=[str,float], has_headers = False)
