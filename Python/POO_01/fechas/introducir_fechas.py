# Pedimos un año y queremos que salga cada uno de los meses del año y que nos diga la fecha del ultimo viernes de cada mes
from datetime import datetime,timedelta
import locale

fecha = input('Dime una fecha (dd/mm/aaaa): ')

fecha = datetime.strptime(fecha,'%d/%m/%Y')

undiamas = timedelta(days=1)

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

# Obtiene todos los jueves del mes #################################################################
while fecha.strftime("%A").capitalize() != 'Jueves':
    fecha = fecha + undiamas
sietediasmas = timedelta(days=7)
mes = fecha.month
while fecha.month == mes:
    print('Fecha: '+ fecha.strftime("%d %B %Y").upper())
    fecha = fecha + sietediasmas
####################################################################################################
# Introducir un año, para cada uno de los meses del año, decir el último viernes de cada mes %b %B