from clases1 import Cuadrado, FG, Rectangulo, Cubo

def imprimir():
    global lista
    for item in lista:
        if(isinstance(item, Cubo)) : print("Volumen ->", item.calcular_volumen())
        print(item)
        print("Perimetro ->",item.calcular_perimetro())
        print("Área ->",item.calcular_area())

def contar(li):
    c = [["Cuadrado",0],["Rectangulo",0],["Cubo",0]]

    for item in li:
        n = 0
        match item.__class__.__name__:
            case "Cuadrado": n = 0
            case "Rectangulo": n = 1
            case "Cubo": n = 2
        c[n][1] += 1
    print(c)

def contar2(li):
    c = {"Cuadrado": 0, "Rectangulo": 0 ,"Cubo": 0}
    for item in li:
        c[item.__class__.__name__] += 1

    for c,v in c.items():
        print(c,"->",v)

def rellenar():
    global lista
    lista.append(Cuadrado(5))
    lista.append(Cuadrado(10))
    lista.append(Cuadrado(20))

    lista.append(Rectangulo(10.50,20.20))

    lista.append(Cubo(5))
    lista.append(Cubo(10))

if __name__ == "__main__":
    lista =[]
    rellenar()
    imprimir()
    contar(lista)
    contar2(lista)