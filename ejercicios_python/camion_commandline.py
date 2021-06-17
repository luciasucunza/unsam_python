# camion_commandline.py

'''
Cuando el archivo ingresado por linea de comando es 'Data/camion.csv' o no ese especifica el archivo en la consola se muestra:
	Costo total: 47671.15

Cuando el archivo ingresado por linea de comando es 'Data/missing.csv' en al cosola se muestra:

	El precio del cajón de Mandarina no puede calcularase ya que no tiene todos los datos
	El precio del cajón de Naranja no puede calcularase ya que no tiene todos los datos
	Costo total: 30381.15
'''

import csv
import sys

def costo_camion(nombre_archivo):
	'Devuelve el costo total de los productos del camion'
	costo_total = 0
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			try:
				costo_total += int(row[1]) * float(row[2])
			except ValueError:
				print(f'El precio del cajón de {row[0]} no puede calcularase ya que no tiene todos los datos')
	return costo_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)