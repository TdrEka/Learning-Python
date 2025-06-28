from datetime import datetime, date, time

ahora = datetime.now()

print(ahora)

fecha_actual = date.today()
print(fecha_actual)

una_fecha = datetime(2024, 8, 12, 13, 46, 23, 1)
print(una_fecha)

mi_cumple = date(1996, 11, 26)

la_hora_pi = time(3, 14, 15)
print(la_hora_pi)

print(una_fecha.year)
print(una_fecha.minute)

ahora.replace(hour=21)


