from abc import ABC,abstractmethod
from Colores import Colores
from ConsumoEnergetico import ConsumoEnergetico

class Electrodomestico(ABC):
    def __init__(self, precio_base:float, color:str, consumo_energetico:str, peso:float):
        self._precio_base = precio_base
        self._color = color
        self._consumo_energetico = consumo_energetico
        self._peso = peso

    def __str__(self):
        return f"Electrodomestico: {self._precio_base:.2f} Color:{self._color} Consumo: {self._consumo_energetico} {self._peso:.2f}kg"

    #GETTER
    def getPrecioBase(self):
        return self._precio_base
    def getColor(self):
        return self._color
    def getConsumoEnergetico(self):
        return self._consumo_energetico
    def getPeso(self):
        return self._peso
    
    #MÉTODOS
    def comprobarConsumoEnergetico(self, letra:ConsumoEnergetico):
        letra = letra.upper()
        
        for consumo in ConsumoEnergetico:
            if letra == consumo.name:
                return letra
        return ConsumoEnergetico.F.name

    def comprobarColor(self, color:Colores):
        color = color.upper()
        
        for color in Colores:
            if color == color.value:
                return color
        return "BLANCO"

    def precioFinal(self):
        # 1. Plus por Consumo (Comparando el string con el nombre del Enum)
        if self._consumo_energetico == ConsumoEnergetico.A.name:
            self._precio_base += 100
        elif self._consumo_energetico == ConsumoEnergetico.B.name:
            self._precio_base += 80
        elif self._consumo_energetico == ConsumoEnergetico.C.name:
            self._precio_base += 60
        elif self._consumo_energetico == ConsumoEnergetico.D.name:
            self._precio_base += 50
        elif self._consumo_energetico == ConsumoEnergetico.E.name:
            self._precio_base += 30
        elif self._consumo_energetico == ConsumoEnergetico.F.name:
            self._precio_base += 10
        
        # 2. Plus por Peso
        if 1 <= self._peso < 19:
            self._precio_base += 10
        elif 19 <= self._peso < 49:
            self._precio_base += 50
        elif 49 <= self._peso < 79:
            self._precio_base += 80
        elif self._peso >= 79:
            self._precio_base += 100
        
        return self._precio_base