from abc import ABC,abstractmethod
import math

class FG(ABC):
    def __init__(self, lado1:float):
        self.lado1 = lado1  #self._lado1 es un atributo protegido
                            #self.__lado1 es un atributo privado
                            #self.lado1 es un atributo publico

    def __str__(self):
        return f"FG: {self.lado1:.2f}"

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Cuadrado(FG):
    def calcular_area(self):
        return math.pow(self.lado1,2)

    def calcular_perimetro(self):
        return 4 * self.lado1

    def __str__(self):
        return f"Cuadrado:\n {self.lado1:.2f}"

class Rectangulo(FG):
    def __init__(self,lado1:float,lado2:float):
        #super().__init__(lado1)
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_perimetro(self):
        return 2 * (self.lado1 * self.lado2)

    def calcular_area(self):
        return self.lado1 * self.lado2

    def __str__(self):
        return f"Reactángulo:\n {self.lado1:.2f} {self.lado2:.2f}"

class Cubo(Cuadrado):

    def calcular_area(self):
        return 6*super().calcular_area()

    def calcular_perimetro(self):
        return 12 * super().calcular_perimetro()

    def calcular_volumen(self):
        return math.pow(self.lado1,3)

    def __str__(self):
        return f"Cubo:\n {self.lado1:.2f}"