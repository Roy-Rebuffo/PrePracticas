from CCuenta import CCuenta

class CCuentaCorriente(CCuenta):
    def __init__(self, nombre:str, cuenta:str, saldo:float, tipoDeInteres:float, transacciones:int,importePorTrans:float,transExentas:int):
        super().__init__(nombre,cuenta,saldo,tipoDeInteres)

        self._transacciones = 0
        self._importePorTrans = importePorTrans
        self._transExentas = transExentas

    def asignarImportePorTrans(self, ipt:int):
        self._importePorTrans = ipt
    def obtenerImportePorTrans(self):
        return self._importePorTrans

    def asignarTransExentas(self, tE:int):
        self._transExentas = tE
    def obtenerTransExentas(self):
        return self._transExentas

    def decrementarTransacciones(self):
        if self._transacciones > 0:
            self._transacciones -=1
    def ingreso(self, i:float):
        i += self._saldo
        self._transacciones +1
    def reintegro(self, r:float):
        r-= self._saldo
        self._transacciones +1
    def comisiones(self):
        if(self._transExentas !=0 ):
            coste_movimientos = self._transacciones - self._transExentas
            self._saldo -= coste_movimientos * self._importePorTrans

            self._transacciones = 0
    def intereses(salf):
        base = self._saldo if self._saldo <=3000 else 3000
        resto = self._saldo - 3000

        interesBase = (base * 0.005) / 12
        interesExtra = (resto * self.obtenerTipoDeInteres()) / 12

        self._saldo += interesBase + interesExtra