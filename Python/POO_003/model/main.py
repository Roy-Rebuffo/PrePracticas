from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

if __name__ == "__main__":
    # Creamos una lista vacía y vamos añadiendo objetos
    lista_electrodomesticos = []
    
    # Añadimos manualmente los 10 objetos para que no se sobreescriban
    lista_electrodomesticos.append(Lavadora(500.0, "blanco", "B", 105.2, 40.0))
    lista_electrodomesticos.append(Television(200.0, "blanco", "B", 105.2, 40.0, True))
    lista_electrodomesticos.append(Electrodomestico(300.0, "blanco", "B", 105.2))
    lista_electrodomesticos.append(Television(400.0, "blanco", "B", 105.2, 40.0, True))
    lista_electrodomesticos.append(Lavadora(600.0, "blanco", "B", 105.2, 40.0))
    lista_electrodomesticos.append(Television(700.0, "blanco", "B", 105.2, 40.0, True))
    lista_electrodomesticos.append(Lavadora(800.0, "blanco", "B", 105.2, 40.0))
    lista_electrodomesticos.append(Television(900.0, "blanco", "B", 105.2, 40.0, True))
    lista_electrodomesticos.append(Lavadora(1000.0, "blanco", "B", 105.2, 40.0))
    lista_electrodomesticos.append(Television(1100.0, "blanco", "B", 105.2, 40.0, True))
    
    #Mostrar el precio de clada clase
    for e in lista_electrodomesticos:
        if isinstance(e, Lavadora):
            print("Lavadora: ",e.precioFinal())
        elif isinstance(e, Television):
            print("Television: ",e.precioFinal())
    
    #Mostrar el precio total de las lavadoras
    total = 0
    for e in lista_electrodomesticos:
        if isinstance(e, Lavadora):
            total += e.precioFinal()
    print("Total precio final lavadoras: ",total)

    #Mostrar el precio total de las televisiones
    total = 0
    for e in lista_electrodomesticos:
        if isinstance(e, Television):
            total += e.precioFinal()
    print("Total precio final televisiones: ",total)

    #Mostrar el precio total de todos los electrodomesticos
    total = 0
    for e in lista_electrodomesticos:
        total += e.precioFinal()
    print("Total precio final electrodomesticos: ",total)