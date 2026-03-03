from CCuentaCorriente import CCuentaCorriente 

class CCuentaCorrienteConIn(CCuentaCorriente):
    def __init__(self, nombre:str, cuenta:str, saldo:float, tipoDeInteres:float, transacciones:int,importePorTrans:float,transExentas:int):
        super().__init__(nombre,cuenta,saldo,tipoDeInteres, transacciones, importePorTrans ,transExentas)
    
    def intereses(self):
        if(self.estado() >= 3000):
            super().self.intereses()