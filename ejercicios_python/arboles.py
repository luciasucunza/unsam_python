# arboles.py
'''
El codigo está separado en tres bloques:
    - Funciones         : Funciones de la clase 2, 3 y 4
    - Programas clase 2 : Programas pedidos en la clase 2 para probar las funciones de la clase
    - Programas clase 3 : Programa pedido en la clase 3 para probar las funciones de la clase
    - Programas clase 4 : Programas pedidos en la clase 2 para plotear de distintas formas los datos obtenidos
        
Para la corrección de la clase 3 correr el primer bloque y el tercero

FUNCIONES CLASE 2:
	def leer_parque(nombre_archivo, parque):			Abre el archivo indicado y devuevle una lista de diccionarios con la información del parque especificado
	def especies(lista_arboles):						Dada una lista de árboles, devuelve el conjunto de especies
	def contar_ejemplares(lista_arboles):				Dada una lista de árboles, devuelve un diccionario donde las claves son las especies y los valores son las cantidades de los mismos (unicamente los 5 que más cantidad tienen)
	def obtener_alturas(lista_arboles, especie):		Dada una lista de árboles y un especie, devuelve una lista de alturas
	def obtener_inclinaciones(lista_arboles, especie):	Dada una lista de árboles y un especie, devuelve una lista de inclinaciones
	def especimen_mas_inclinado(lista_arboles):			Dada una lista de árboles, devuleve la especie que tiene el ejemplar más inclinado y su inclinación
	def especie_promedio_mas_inclinada(lista_arboles):	Dada una lista de árboles, devuelve la especie que tiene en promedio la mayor inclinación y el valor del promedio

FUNCIONES CLASE 3:
    def leer_arboles(nombre_archivo):                   Abre el archivo indicado y devuelve una lista de diccionarios con la infromación de los árboles de toda la ciudad
    def medidas_de_especies(especies, arboleda):        Dada una lista de arboles y una lista de especies, devuelve un diccionario cuyas palabras claves son las especies y los valores asociados son las aluras y los diámetros de todos lo árboles de esa especie
    
'''

#%%

import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np

#------------Función:leer_parque------------
def leer_parque(nombre_archivo, parque):
	lista_arboles=[]
	with open(nombre_archivo, 'rt', encoding="utf8") as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record = dict(zip(headers, row))
			if record['espacio_ve'] == parque:
				lote = {	
					'long' : record['long'],
					'lat' : record['lat'],
					'id_arbol' : record['id_arbol'],
					'altura_tot' : float(record['altura_tot']),
					'diametro' : record['diametro'],
					'inclinacio' : float(record['inclinacio']),
					'id_especie' : record['id_especie'],
					'nombre_com' : record['nombre_com'],
					'nombre_cie' : record['nombre_cie'],
					'espacio_ve' : record['espacio_ve'], 
					'ubicacion' : record['ubicacion'], 
					'nombre_fam' : record['nombre_fam'], 
					'nombre_gen' : record['nombre_gen'], 
					'origen' : record['origen'], 
					'coord_x' : record['coord_x'],
					'coord_y' : record['coord_y'] 
					}
				lista_arboles.append(lote)
	return lista_arboles

#------------Función:especies------------
def especies(lista_arboles):
	especies = []
	for arbol in lista_arboles:
		especies.append(arbol['nombre_com'])
	return set(especies)

#------------Función:contar_ejemplares------------
def contar_ejemplares(lista_arboles):
	ejemplares = Counter()
	for arbol in lista_arboles:
		ejemplares[arbol['nombre_com']] += 1
	mas_frecuentes = ejemplares.most_common(5)
	return dict(mas_frecuentes)

#------------Función:obtener_alturas------------
def obtener_alturas(lista_arboles, especie):
	alturas = []
	for arbol in lista_arboles:
		if arbol['nombre_com'] == especie:
			alturas.append(arbol['altura_tot'])
	return alturas

#------------Función:obtener_inclinaciones------------
def obtener_inclinaciones(lista_arboles, especie):
	inclinaciones = []
	for arbol in lista_arboles:
		if arbol['nombre_com'] == especie:
			inclinaciones.append(arbol['inclinacio'])
	return inclinaciones

#------------Función:especimen_mas_inclinado------------
def especimen_mas_inclinado(lista_arboles):
	mas_inclinado = { 'especie':'', 'inclinacion':0.0}
	cont_especies = especies(lista_arboles)
	for especie in cont_especies:
		inclinaciones = obtener_inclinaciones(lista_arboles, especie)
		if max(inclinaciones) > mas_inclinado['inclinacion']:
			mas_inclinado['especie'] = especie
			mas_inclinado['inclinacion'] = max(inclinaciones)
	return mas_inclinado['especie'], mas_inclinado['inclinacion']

#------------Función:especimen_promedio_mas_inclinado------------
def especie_promedio_mas_inclinada(lista_arboles):
	prom_mas_inclinado = { 'especie':'', 'inclinacion':0.0}
	cont_especies = especies(lista_arboles)
	for especie in cont_especies:
		inclinaciones = obtener_inclinaciones(lista_arboles, especie)
		prom_inclinaciones = sum(inclinaciones)/len(inclinaciones)
		if prom_inclinaciones > prom_mas_inclinado['inclinacion']:
			prom_mas_inclinado['especie'] = especie
			prom_mas_inclinado['inclinacion'] = prom_inclinaciones 
	return prom_mas_inclinado['especie'], prom_mas_inclinado['inclinacion']

#------------Función:leer_arboles------------
def leer_arboles(nombre_archivo):
    lista_arboles = []
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        lista_arboles = [{ ncolumna : val for ncolumna, val in zip(headers, row)} for row in rows]
        return lista_arboles
  
#------------Función:leer_arboles------------
def medidas_de_especies(especies, arboleda):
    dicc = {especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }
    return dicc
    
#%%   
#------------Programas Clase 2 ------------
archivo = 'Data/arbolado.csv'
parques = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')

#------------Programa:Frecuentes------------
for parque in parques:
	lista = leer_parque(archivo, parque)
	dicc = contar_ejemplares(lista)
	print('---------------------------------------------')
	cant = 'Cantidad'
	print(f'{parque:<33s} {cant:<10s}')
	print('---------------------------------------------')
	print(f'{list(dicc)[0]:<33s} {dicc[list(dicc)[0]]:<10d}')
	print(f'{list(dicc)[1]:<33s} {dicc[list(dicc)[1]]:<10d}')
	print(f'{list(dicc)[2]:<33s} {dicc[list(dicc)[2]]:<10d}')
	print(f'{list(dicc)[3]:<33s} {dicc[list(dicc)[3]]:<10d}')
	print(f'{list(dicc)[4]:<33s} {dicc[list(dicc)[4]]:<10d}')

#------------Programa:Altura------------
altura_max = {}
altura_prom = {}
especie = 'Jacarandá'
for parque in parques:
	lista = leer_parque(archivo, parque)
	alturas = obtener_alturas(lista, especie)
	altura_max[parque] = max(alturas)
	altura_prom[parque] = sum(alturas)/len(alturas)
print('---------------------------------------------')
print('Parque          Altura Max        Promedio')
print('---------------------------------------------')
print(f'{parques[0]:<16s} {altura_max[parques[0]]:<16.2f} {altura_prom[parques[0]]:<11.2f}')
print(f'{parques[1]:<16s} {altura_max[parques[1]]:<16.2f} {altura_prom[parques[1]]:<11.2f}')
print(f'{parques[2]:<16s} {altura_max[parques[2]]:<16.2f} {altura_prom[parques[2]]:<11.2f}')
   
#------------Programa:Inclinación Máxima------------
inclinacion_max = {}
esp_inclinacion_max = {}
for parque in parques:
	lista = leer_parque(archivo, parque)
	esp_inclinacion_max[parque], inclinacion_max[parque] = especimen_mas_inclinado(lista)
print('---------------------------------------------')
print('Parque          Inclinación Máx   Especie')
print('---------------------------------------------')
print(f'{parques[0]:<16s} {inclinacion_max[parques[0]]:<16.1f} {esp_inclinacion_max[parques[0]]:<20s}')
print(f'{parques[1]:<16s} {inclinacion_max[parques[1]]:<16.1f} {esp_inclinacion_max[parques[1]]:<20s}')
print(f'{parques[2]:<16s} {inclinacion_max[parques[2]]:<16.1f} {esp_inclinacion_max[parques[2]]:<20s}')
  
#------------Programa:Inclinación Promedio------------
inc_max_prom = {}
esp_inc_max_prom = {}
for parque in parques:
	lista = leer_parque(archivo, parque)
	esp_inc_max_prom[parque], inc_max_prom[parque] = especie_promedio_mas_inclinada(lista)
print('---------------------------------------------')
print('Parque          Inclinación Máx   Especie')
print('---------------------------------------------')		
print(f'{parques[0]:<16s} {inc_max_prom[parques[0]]:<16.1f} {esp_inc_max_prom[parques[0]]:<20s}')
print(f'{parques[1]:<16s} {inc_max_prom[parques[1]]:<16.1f} {esp_inc_max_prom[parques[1]]:<20s}')
print(f'{parques[2]:<16s} {inc_max_prom[parques[2]]:<16.1f} {esp_inc_max_prom[parques[2]]:<20s}')
  
    
#%%   
#------------Programas Clase 3 ------------
arboleda = leer_arboles('Data/arbolado.csv')
esp = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
d = medidas_de_especies(esp, arboleda)

print('Control por tamaño de listas')
for especie in esp:
    print(especie, ':', len(d[especie]) )
    
    
#%%
#------------Programas Clase 4 ------------
nombre_archivo = 'Data/arbolado.csv'
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)

altos =[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos, bins = 100)


#------------Programa:Relación diámetro-alto para Jacarandás------------
dic_med_jacaranda = medidas_de_especies(['Jacarandá'], arboleda)
arr_med_jacaranda = np.array(dic_med_jacaranda['Jacarandá'])
d =  arr_med_jacaranda[:,0]
h =  arr_med_jacaranda[:,1]
plt.figure()
plt.scatter(d, h, c='red', alpha=0.1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")


#------------Programa:Relación diámetro-alto para Eucalipto, Palo borracho rosado y Jacarandás------------
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

arr_med_eucalipto = np.array(medidas['Eucalipto'])
d_euc =  arr_med_eucalipto[:,0]
h_euc =  arr_med_eucalipto[:,1]
arr_med_palo = np.array(medidas['Palo borracho rosado'])
d_pal =  arr_med_palo[:,0]
h_pal =  arr_med_palo[:,1]
arr_med_jacaranda = np.array(medidas['Jacarandá'])
d_jac =  arr_med_jacaranda[:,0]
h_jac =  arr_med_jacaranda[:,1]

plt.figure()
plt.scatter(d_euc, h_euc, c = 'blue', alpha=0.1)
plt.scatter(d_pal, h_pal, c = 'green', alpha=0.1)
plt.scatter(d_jac, h_jac, c = 'red', alpha=0.1)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para tres especies")
plt.xlim(0,30) 
plt.ylim(0,100) 



