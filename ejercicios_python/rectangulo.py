# rectangulo.py

    
#%%
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
    
#%%
class Rectangulo(): 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return f'({self.p1}, {self.p2})'
    
    def __repr__(self):
        return f'Rectangulo({self.p1}, {self.p2})'
        
    def base(self):
        return abs(self.p1.x - self.p2.x)
    
    def altura(self):
        return abs(self.p1.y - self.p2.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def desplazamiento(self, desplazamiento):
        self.p1 = self.p1 + desplazamiento
        self.p2 = self.p2 + desplazamiento
        
        
        # NO FUNCIONA BIEN, REVISAR
    def rotar(self):
        if self.p1.x < self.p2.x:
            self.p1.x += (self.base()+self.altura())
        else:
            self.p2.x += (self.base()+self.altura())
            
        if self.p1.y > self.p2.y:
            self.p1.y += (self.base()-self.altura())
        else:
            self.p2.y += (self.base()-self.altura())