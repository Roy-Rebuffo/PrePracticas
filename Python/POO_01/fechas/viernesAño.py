from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import locale

def ultimoViernes(fecha:datetime):
    unmesmas = relativedelta(months = 1, days =-1) # ÚLTIMO DÍA DEL MES
    undiamenos = timedelta(days=-1)
    fecha = fecha + unmesmas
    while fecha.strftime("%A").capitalize() != 'Viernes':
        fecha = fecha + undiamenos
    return fecha

def fechas(fecha:datetime):
    for i in range(1,13):
        fecha = fecha.replace(month=i)
        print(f'{fecha.strftime('%B').capitalize():15s} {ultimoViernes(fecha).strftime('%d/%m/%Y')}')

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    anno=int(input("Dime un año: "))
    f = datetime(anno,1,1)
    fechas(f)