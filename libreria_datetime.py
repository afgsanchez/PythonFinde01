# La libreria datetime nos permite manipular fechas de forma sencilla.
# Veremos las funciones datetime.now, date.today, date y datetime

# Importamos la libreria.
import datetime

print()
# Funcion datetime.now, retorna la fecha y la hora de ahora mismo
print("datetime.now - Fecha y hora actual: ", datetime.datetime.now())
print()
# Funcion date.today, retorna el dia de hoy.
print("date.today - Fecha actual: ", datetime.date.today())
print()
# Funcion date, nos permite crear un objeto del tipo fecha pasandole la fecha que nosotros queremos.
fecha = datetime.date(2024, 5, 19)
print("date - La fecha que le hemos seteado es: ", fecha)
print()
# Funcion datetime, nos permite crear un objeto del tipo datetime pasandole la fecha  y hora (incluidos los microsegundos si queremos) que nosotros queremos.
fechahora= datetime.datetime(2023, 5, 19, 23, 5, 15, 123456)
print("datetime - Fecha y hora seteada: ", fechahora)

# Ahora vamos a ver un ejercicio para acceder a los elementos que componen la fecha y la hora de forma individual, es decir, 
# la hora, los minutos, segundos, dia, mes, año...
fecha_actual = datetime.datetime.now()
print(fecha_actual)
print("Año: ", fecha_actual.year)
print("Mes: ", fecha_actual.month)
print("Dia: ", fecha_actual.day)
print("Hora: ", fecha_actual.hour)
print("Minutos: ", fecha_actual.minute)
print("Segundos: ", fecha_actual.second)
print("Milisegundos: ", fecha_actual.microsecond)
print()

# Ahora veremos dos ejercicios para calcular la diferencia entre dos objetos datetime, restando.
# Tiempo de diferencia entre fechas, nos devuelve el resultado en dias, horas, minutos, segundos...
fin = datetime.datetime.now()
inicio = datetime.datetime(2016, 2, 21, 14, 00, 00, 123456)
print("Resta de fechas:")
print("1.- ", fin)
print("2.- ", inicio)
resultado = fin - inicio
print("Resultado: ", resultado)
print()

# Un ejemplo util es calcular la edad segun la fecha actual y la fecha de nacimiento.
nacimiento = datetime.date(1975, 12, 4)
ahora = datetime.date.today()
print("Nacido en: ", nacimiento)
print("Hoy es: ", ahora)
años = ahora - nacimiento # Esto nos devuelve la diferencia en dias, horas, minutos, segundos
años = años.days / 365.25 # Añadimos el metodo .days para que solo nos tome los dias, sin horas ni minutos, etc...
print(f"Tienes {años} años.") 
