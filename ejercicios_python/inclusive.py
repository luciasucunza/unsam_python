#inclusive.py

frase = 'todos somos programadores'
# frase = '¿cómo transmitir a los otros el infinito Aleph?'
# frase = 'Todos, tu también'                                       
# En este útlimo caso falla debido a la coma, la primera cadena será 'Todos,'
# Por lo tanto, la posción de la 'o' no es la útlima ni anteúlitma.

palabras = frase.split()

for palabra in palabras:
	if len(palabra)>=2:
	    if palabra[-1:] == 'o':
	        i = palabras.index(palabra) 
	        palabras[i] = palabra[:-1] + 'e'    
	    elif palabra[-2:-1] == 'o':
	        i = palabras.index(palabra) 
	        palabras[i] = palabra[:-2] + 'e' + palabra[-1:]
	        
frase_t=' '.join(palabras)
print(frase_t)
