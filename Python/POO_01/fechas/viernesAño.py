from datetime import datetime,timedelta
import locale

def ultimoViernes(fecha:datetime):
    unmesmas = timedelta(month = 1)
    undiamenos = timedelta(days=-1)
    fecha = fecha + unmesmas + undiamenos

def fechas(fecha:datetime):
    for i in range(1,13):
        fecha = fecha.replace(month=i)
        print(fecha.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    anno=int(input("Dime un año: "))
    f = datetime(anno,1,1)
    fechas(f)