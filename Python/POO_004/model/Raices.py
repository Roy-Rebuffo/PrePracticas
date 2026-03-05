class Raices():
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c
    
    def __str__(self):
        return f"{self._a}x^2 + {self._b}x + {self._c} = 0"

    #Una ecuacion de 2º grado se cumple si el discriminante(lo que está dentro de la raiz cuadrada) es mayor o igual a 0
    def getDiscriminante(self):
        return self._b**2 - 4*self._a*self._c
    
    def obtenerRaices(self):
        if self.getDiscriminante() > 0:
            return (-self._b + self.getDiscriminante()**0.5) / (2*self._a), (-self._b - self.getDiscriminante()**0.5) / (2*self._a)
        else:
            return None
    def obtenerRaiz(self):
        if self.getDiscriminante() == 0:
            return (-self._b) / (2*self._a)
        else:
            return None
    def tieneRaices(self):
        return self.getDiscriminante() >= 0
    def tieneRaiz(self):
        return self.getDiscriminante() == 0
    def calcular(self):
        if self.tieneRaices():
            return self.obtenerRaices()
        elif self.tieneRaiz():
            return self.obtenerRaiz()
        else:
            return None