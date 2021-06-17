# fileparse.py
'''
Dejé los comentarios que estaban en el código de la clase
'''

import csv
 
def parse_csv(lines, select = None, types = None, has_headers=True, silence_errors = True):
    '''
    Parsea un objeto en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, debe ser una lista de nombres de las columnas a considerar.
    
    '''    
    # Si me seleccionan ciertas columnas pero no hay encabezados levanto una excepción
    if select and not has_headers:
        raise RuntimeError("Para seleccionar columnas, necesito encabezados.")
        
    filas = csv.reader(lines)

    if has_headers:
        # Lee los encabezados del archivo
        encabezados = next(filas)
        # Si se indicó un selector de columnas, buscar los índices de las columnas especificadas.
        # En ese caso achicar el conjunto de encabezados para diccionarios
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
            
    # Lista donde se irán guardando los elementos
    registros = []
    
    for i, fila in enumerate(filas, 1):
        if not fila:    # Saltear filas vacías
            continue
        
        # Utiliza los tipos pasados, o los escritos por default
        if types:
            try:
                fila = [func(val) for func, val in zip(types, fila) ]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {i}: No pude convertir {fila}')
                    print(f'Row {i}: Motivo: {e}')

        
        # Si hay headers genera un diccionario de acuerdo a los encabezados
        if has_headers:
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
        # En caso de no haber headers el elemento agregado es una tupla en lugar de un diccionario
        else:
            registro = tuple(fila)
        registros.append(registro)

    return registros
