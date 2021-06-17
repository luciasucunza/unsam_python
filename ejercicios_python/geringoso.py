#geringoso.py

cadena = 'Geringoso'
#cadena = 'apa'
#cadena = 'boligoma'

capadepenapa = ''
for c in cadena:
    
    capadepenapa = capadepenapa + c
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':			#if c in 'aeiouAEIOU'
        capadepenapa = capadepenapa+'p'+c
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':			
        capadepenapa = capadepenapa+'P'+c 
        
# print(capadepenapa)