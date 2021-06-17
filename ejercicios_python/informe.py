# informe.py

import fileparse as fp
import lote
import formato_tabla

#%%------------Función:leer_camion------------
def leer_camion(nombre_archivo):
    ''' Obtiene una lista con la infromación de un camión alojada en un archivo.
    
        Pre: el archivo tiene que estar en formato csv, tener encabezados y
            estar formado por 3 columnas, una de nombres, una de enteros y una
            de números reales.
        Pos: Devuelve una lista, con todos los datos del camion orgnaizados en
            instancias de Lote.
    '''
    with open(nombre_archivo) as f:
        camion = fp.parse_csv(f, select=['nombre','cajones','precio'], types=[str,int,float])
    
    camion = [ lote.Lote(c['nombre'], c['cajones'], c['precio']) for c in camion]
    return camion



#%%#------------Función:leer_precios------------
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


#%%#------------Función:hacer_informe()------------
def hacer_informe(lista_cajones, dicc_precios):
    ''' Obtiene una lista de tuplas con los datos correspondientes a cada fruta
         Los datos corresponden a la cantidad de cajones, el precio y la dife-
         rencia entre el precio de venta y el de compra.
         
        Pre: lista_cajones debe ser una lista de obejtos Lote, que incluya las
            claves 'nombre', 'cajones' y 'precios'.
             dicc_precios debe ser un dicciónario de precios y nombres.
             Todos los nombres de frutas de lista_cajones deben estar en el 
            diccionario de precios.
        Pos: Devuelve una lista de tuplas, las tuplas contienen nombre, precio 
            y diferencia entre el precio de venta y el de compra
    '''
    lista_tuplas = []
    for d in lista_cajones:
        tupla = ( d.nombre, d.cajones, d.precio, dicc_precios[d.nombre]-d.precio)
        lista_tuplas.append(tupla)
    return lista_tuplas


#%%#------------Función:imprimir_informe()------------
def imprimir_informe(data_informe, formateador):
    ''' Imprime de forma prolija un infrome.
    
        Pre: Debe recibir una lista de tuplas, el formato de estas últimas debe
            ser ('Nombre', 'Cajones', 'Precio', 'Cambio')
        Pos: Imprime en la consola el informe

    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
        

#%%#------------Función:imprimir_informe()------------
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    ''' Calcula e imprime un informe con los datos de un archivo con datos de 
        un camion y un archivo con los precios y
        
        Pre: Los archivos deben existir y tene los formatos explicados en las
            funciones 'leer_camion' y 'leer_precios'
        Pos: Imprime en la consola el informe

    '''
    # Leer archivos con datos
    camion  = leer_camion(nombre_archivo_camion)  
    
    # Crear los datos para el informe
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador )


#%%#------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) == 3:
        camion = parametros[1]
        precios = parametros[2]
        informe_camion(camion, precios)
    elif len(parametros) == 4:
        camion = parametros[1]
        precios = parametros[2]
        formato = parametros[3]
        informe_camion(camion, precios, formato)
    else:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios fmt (opcional')


#%%

if __name__ == '__main__':
    import sys
    main(sys.argv)
