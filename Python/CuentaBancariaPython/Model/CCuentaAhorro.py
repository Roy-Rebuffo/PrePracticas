from datetime import datetime
from CCuenta import CCuenta
class CCuentaAhorro(CCuenta):
    def __init__(self, nombre:str, cuenta:str, saldo:float, tipoDeInteres:float, _cuotaMantenimiento:float):
        super().__init__(nombre,cuenta,saldo,tipoDeInteres)

        self._cuotaMantenimiento = cuotaMantenimiento
    
    #SETTER
    def asignarCuotaManten(self, cM:float):
        self._cuotaMantenimiento = cM
    #GETTER
    def obtenerCuentaMantenimiento(self):
        return self._cuotaMantenimiento

    #SOBREESCRIBIMOS LOS MÉTODOS ABSTRACTOS
    def comisiones(self):
        self._saldo -= self._cuotaMantenimiento

    def intereses(self):
        hoy = datetime.now()
        if hot.day == 1:
            interesMes = self._saldo * self.obtenerTipoDeInteres() / 12 / 100
            self._saldo += interesMes
    