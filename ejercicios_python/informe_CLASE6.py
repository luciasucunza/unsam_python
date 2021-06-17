# informe.py

import fileparse as fp

#%%
#------------Función:leer_camion------------
def leer_camion(nombre_archivo):
    ''' Obtiene una lista con la infromación de un camión alojada en un archivo.
    
        Pre: el archivo tiene que estar en formato csv, tener encabezados y
            estar formado por 3 columnas, una de nombres, una de enteros y una
            de números reales.
        Pos: Devuelve una lista, con todos los datos del camion,
            organizados en diccionarios.
    '''
    with open(nombre_archivo) as f:
        camion = fp.parse_csv(f, select=['nombre','cajones','precio'], types=[str,int,float])
    return camion


#------------Función:leer_precios------------
def leer_precios(nombre_archivo):
    ''' Obtiene un diccionario con la infromación de precios alojada en un 
         archivo formato csv.
    
        Pre: el archivo tiene que estar en formato csv, no tener encabezados y
            estar formado por una columna de nombres y una de precios.
        Pos: Devuelve una lista, con todos los datos del camion,
            organizados en diccionarios.
    '''
    with open(nombre_archivo) as f:
        precios = fp.parse_csv(f, types=[str, float], has_headers=False)
    return dict(precios)


#------------Función:hacer_informe()------------
def hacer_informe(lista_cajones, dicc_precios):
    ''' Obtiene una lista de tuplas con los datos correspondientes a cada fruta
         Los datos corresponden a la cantidad de cajones, el precio y la dife-
         rencia entre el precio de venta y el de compra.
         
        Pre: lista_cajones debe ser una lista de diccionarios, que incluta las
            claves 'nombre', 'cajones' y 'precios'.
             dicc_precios debe ser un dicciónario de precios y nombres.
             Todos los nombres de frutas de lista_cajones deben estar en el 
            diccionario de precios.
        Pos: Devuelve una lista de tuplas, las tuplas contienen nombre, precio 
            y diferencia entre el precio de venta y el de compra
    '''
    lista_tuplas = []
    for d in lista_cajones:
        tupla = ( d['nombre'], d['cajones'], ('$'+str(d['precio'])), dicc_precios[d['nombre']]-d['precio'])
        lista_tuplas.append(tupla)
    return lista_tuplas


#------------Función:imprimir_informe()------------
def imprimir_informe(informe):
    ''' Imprime de forma prolija un infrome.
    
        Pre: Debe recibir una lista de tuplas, el formato de estas últimas debe
            ser ('Nombre', 'Cajones', 'Precio', 'Cambio')
        Pos: Imprime en la consola el informe

    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    tira = '----------'
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{tira:>10s} {tira:>10s} {tira:>10s} {tira:>10s}')   
    for row in informe:
        print('%10s %10d %10s %10.2f' %row)
        
        
#------------Función:imprimir_informe()------------
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    ''' Calcula e imprime un informe con los datos de un archivo con datos de 
        un camion y un archivo con los precios y
        
        Pre: Los archivos deben existir y tene los formatos explicados en las
            funciones 'leer_camion' y 'leer_precios'
        Pos: Imprime en la consola el informe

    '''
    camion  = leer_camion(nombre_archivo_camion)  
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


#------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    precios = parametros[2]
    informe_camion(camion, precios)


#%%
informe_camion('Data/camion.csv','Data/precios.csv')

# if __name__ == '__main__':
#     import sys
#     main(sys.argv)
    
    
    
