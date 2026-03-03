from CCuenta import CCuenta
class CBanco(CCuenta):
    def __init__(self):
        self.__clientes = []

    def obtenerClientes(self):
        return self.__clientes
    def insertarCliente(self, cuenta):
        self.__clientes.append(cuenta)
    def eliminarCliente(self, numCuenta):
        self.__clientes.remove(self.obtenerCuenta() == numCuenta)
    def longitud():
        return len(self.__clientes)
    def buscar(self, texto):
        resultados = []
        valor = valor.lower()

        for c in self.__clientes:
            if(valor in c.obtenerNombre().lower() or valor in c.obtenerCuenta().lower()):
                resultados.append(c)
        return resultados
    def mantenimientoMensual(self):
        for c in self.__clientes:
            self.intereses()
            self.comisiones()
        print(f'Realizado el mantenimiento mensual para {self.longitud()} clientes')