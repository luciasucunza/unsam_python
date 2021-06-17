# informe_funciones.py

import csv
import fileparse as fp

#------------Función:leer_camion------------
def leer_camion(nombre_archivo):
    camion = fp.parse_csv(nombre_archivo)
    return camion

#------------Función:leer_precios------------
def leer_precios(nombre_archivo):
	'Devuelve los precios en forma de dic  cionario'
	precios = fp.parse_csv(nombre_archivo, types=[str, float], has_headers=False)
	return dict(precios)

#------------Función:hacer_informe()------------
def hacer_informe(lista_cajones, dicc_precios ):
	lista_tuplas = []
	for d in lista_cajones:
		tupla = ( d['nombre'], d['cajones'], ('$'+str(d['precio'])), dicc_precios[d['nombre']]-d['precio'])
		lista_tuplas.append(tupla)
	return lista_tuplas

#------------Función:imprimir_informe()------------
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    tira = '----------'
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{tira:>10s} {tira:>10s} {tira:>10s} {tira:>10s}')   
    for row in informe:
        print('%10s %10d %10s %10.2f' %row)
        
#------------Función:imprimir_informe()------------
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion  = leer_camion(nombre_archivo_camion)  
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
