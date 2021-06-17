# lote.py


#%%
class Lote:
    '''
    Crear un lote con nombre, cantidad y precio del producto
    '''

    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
    
    def costo(self):
        return self.cajones*self.precio

    def vender(self, venta):
        self.cajones -= venta


#%%        
class MiLote(Lote):
    '''
    Crear un lote con nombre, cantidad y precio del producto, que permite 
    rematar todo el producto con un método
    '''
    def rematar(self):
        self.vender(self.cajones)
        
