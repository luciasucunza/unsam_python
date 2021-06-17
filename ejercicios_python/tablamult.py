# tablamult.py


headers = (0,1,2,3,4,5,6,7,8,9)

lista_dicc=[]
for i in headers:
	dicc = dict.fromkeys(headers,0)
	for d in dicc:
		if d > 0:
			dicc[d] = dicc[d-1] + i 
	lista_dicc.append(dicc)


cad_headers = f'     {headers[0]:>3d} {headers[1]:>3d} {headers[2]:>3d} {headers[3]:>3d} {headers[4]:>3d} {headers[5]:>3d} {headers[6]:>3d} {headers[7]:>3d} {headers[8]:>3d} {headers[9]:>3d}'
print(cad_headers)
print('---------------------------------------------')	
for d in lista_dicc:
	cad_fila = f' {d[1]:>1d}:  {d[0]:>3d} {d[1]:>3d} {d[2]:>3d} {d[3]:>3d} {d[4]:>3d} {d[5]:>3d} {d[6]:>3d} {d[7]:>3d} {d[8]:>3d} {d[9]:>3d}'
	print(cad_fila)