# tabla_informe.py

'''
Creo que a lidea de edf hacer_informe aera que imprima todo de una, es decir:
def hacer_informe(archivo_camion, archivo_precio):
	camion  = leer_camion(archivo_camion)  
	precios = leer_precios('archivo_precio)
	headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	tira = '----------'
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(f'{tira:>10s} {tira:>10s} {tira:>10s} {tira:>10s}')
	lista_tuplas = []
	for r in lista_cajones:
		tupla = ( d['nombre'], d['cajones'], ('$'+str(d['precio'])), precios[d['nombre']]-d['precio'])
		print('%10s %10d %10s %10.2f' %tupla)
'''


import csv

#------------Función:leer_camion------------
def leer_camion(nombre_archivo):
	'Devuelve una lista de diccionarios'
	camion = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for n_row, row in enumerate(rows, start=1):
			record = dict(zip(headers, row))
			try:
				lote = { 'nombre' : record['nombre'], 'cajones': int(record['cajones']), 'precio' : float(record['precio'])}
				camion.append(lote)
			except IndexError:
				flag_error = f'Fila {n_row}: No pude interpretar: {row}'
	return camion

#------------Función:leer_precios------------
def leer_precios(nombre_archivo):
	'Devuelve los precios en forma de diccionario'
	precios = {}
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		for n_row, row in enumerate(rows, start=1):
			try:
				precios[row[0]] = float(row[1])
			except IndexError:
				flag_error = f'Fila {n_row}: No pude interpretar: {row}'
	return precios

#------------Función:hacer_informe()------------
def hacer_informe(lista_cajones, dicc_precios ):
	lista_tuplas = []
	for d in lista_cajones:
		tupla = ( d['nombre'], d['cajones'], ('$'+str(d['precio'])), dicc_precios[d['nombre']]-d['precio'])
		lista_tuplas.append(tupla)
	return lista_tuplas


#------------Programa:Balance------------
camion  = leer_camion('Data/fecha_camion.csv')  
precios = leer_precios('Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
tira = '----------'
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{tira:>10s} {tira:>10s} {tira:>10s} {tira:>10s}')
for r in informe:
    print('%10s %10d %10s %10.2f' %r)