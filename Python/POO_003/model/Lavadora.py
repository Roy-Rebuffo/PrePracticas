from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, precio_base: float, color: str, consumo_energetico: str, peso: float, carga: float):
        super().__init__(precio_base, color, consumo_energetico, peso)
        self.carga = carga

    def getCarga(self):
        return self.carga
    
    def precioFinal(self):
        super().precioFinal()
        if self.carga >= 30:
            self._precio_base += 50
        return self._precio_base
    