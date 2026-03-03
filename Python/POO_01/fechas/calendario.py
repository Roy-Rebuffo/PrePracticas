import calendar
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')
año = int(input("Introducir año"))

print(calendar.calendar(año,2,1,6,4))