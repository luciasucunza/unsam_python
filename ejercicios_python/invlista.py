#invlista.py

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida = [e]+invertida
    return invertida

# invertir_lista([1, 2, 3, 4, 5])
# invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
