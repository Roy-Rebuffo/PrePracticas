from abc import ABC,abstractmethod

class CCuenta(ABC):
    def __init__(self, nombre:str, cuenta:str, saldo:float, tipoDeInteres:float):
        self._nombre = nombre
        self._cuenta = cuenta
        self._saldo = saldo
        self._tipoDeInteres = tipoDeInteres

    def __str__(self):
        return f"CCuenta: {self._nombre}{self._cuenta}{self._saldo:.2f}{self._tipoDeInteres:.2f}"

    #SETTER
    def asignarNombre(self, n:str):
        self._nombre = n
    #GETTER
    def obtenerNombre(self):
        return self._nombre

    def asignarCuenta(self, c:float):
        self._cuenta = c
    def obtenerCuenta(self):
        return self._cuenta

    def asignarTipoInteres(slef, tdi:float):
        self._tipoDeInteres = tdi
    def obtenerTipoDeInteres(self):
        return self._tipoDeInteres
    
    def estado(self):
        return self._saldo
    
    def ingreso(self, cantidad:float):
        cantidad += self._saldo
    def reintegro(self, cantidad:float):
        cantidad -= self._saldo
    
    @abstractmethod
    def comisiones(self):
        pass
    @abstractmethod
    def intereses(self):
        pass