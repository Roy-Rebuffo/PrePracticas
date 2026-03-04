from Electrodomestico import Electrodomestico

class Television(Electrodomestico):
    def __init__(self, precio_base: float, color: str, consumo_energetico: str, peso: float, resolucion: int, tdt:bool):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.resolucion = resolucion
        self.tdt = tdt
    
    def getResolucion(self):
        return self.resolucion
    def getTdt(self):
        return self.tdt
    
    def precioFinal(self):
        super().precioFinal()
        if self.resolucion > 40:
            self._precio_base += self._precio_base * 0.3
        if self.tdt:
            self._precio_base += 50
        return self._precio_base