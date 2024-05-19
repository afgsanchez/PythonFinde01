# La libreria math permite incluir en los programas funciones y constantes matemáticas complejas.

# Importamos la libreria.
import math

# PRIMERO VAMOS A VER LAS 5 FUCNIONES MAS IMPORTANTES
# pi, e, tau, inf, nan
print()
# Fucion pi, tiene el valor constante de pi
print("pi - El valor de PI es: ", math.pi)
print()
# Funcion e, tiene el valor de la consante e
print("e - El valor de la constante e es: ", math.e)
print()
# Funcion tau, tiene el valor de la constante t
print("tau - El valor de la constante t es: ", math.tau)
print()
# Funcion inf, representacion del valor infinito
print("inf - El valor de infinito es: ", math.inf)
print()
# Funcion nan, representacion de NaN (Not a Number)
print("nan - El valor de NaN es: ", math.nan)
print()

# AHORA EL RESTO DE FUNCIONES
print()
#Funcion fabs, retorna el valor absoluto del numero especificado como parametro.
print("fabs - valor absoluto del numero -5: ", math.fabs(-5))
print()
# Funcion factorial, calcula la factorial del numero dado en parametro.
print("factorial - calcula la factorial del numero 65: ", math.factorial(8))
print()
# Funcion gcd, calcula el maximo comun divisor de dos numeros dados en parametro.
print("gcd - Maximo Comun Divisor de los numeros 12 y 85: ", math.gcd(12, 85))
print()
# Funcion isnam, comprueba si el parametro no es un numero. Retorna False si es número y True si no es número.
print("isnam - Comprueba si un valor no es un numero, si no es numero devuelve True, \n\tsi es numero devuelve False, le paso como parametro '8': ", math.isnan(8))
print()
# Funcion log, calcula el logaritmo en base X del numero dado por parámetro. Necesita dos parametros.
# El primero es el número del que se quiere calcular el logaritmo, el segundo es la base del logaritmo.
print("log - logaritmo en base X, en este ejemplo del numero 5 con base 3: ", math.log(5, 3))
print()
# Funcion pow, calcula la potencia de numero dado por parametro, Necesita dos parametros.
# El primero es la base, el segundo es el exponente.
print("pow - potencia del numero 5 con exponente 3: ", math.pow(5, 3))
print()
# Fucion sqrt, calcula la raiz cuadrada del numero especificado en el paramentro.
print("sqrt - Raiz Cuadrara del numero 456: ", math.sqrt(456))
print()
# Funcion acos, calcula ArcoCoseno en radiantes del angulo pasado en parametro.
print("acos - ArcoCoseno en radianes del angulo 1: ", math.degrees(math.acos(1)))
print()
# Funcion asin, calcula Arcoseno en radiantes del angulo pasado en parametro.
print("asin - Arcoseno en radianes del angulo 1: ", math.degrees(math.asin(1)))
print()
# Funcion atan, calcula Arcotangente en radiantes del angulo pasado en parametro.
print("asin - Arcotangente en radiants del angulo 1: ", math.degrees(math.atan(1)))
print()
# Funcion cos, calcula Coseno en radiantes del angulo pasado en parametro.
print("cos - Coseno en radianes del angulo 180: ", math.cos(math.radians(180)))
print()
# Funcion sin, calcula seno en radiantes del angulo pasado en parametro.
print("sin - Seno en radianes del angulo 180: ", math.sin(math.radians(180)))
print()
# Funcion tan, calcula Tangente en radiantes del angulo pasado en parametro.
print("tan - Tangente en radianes del angulo 180: ", math.tan(math.radians(180)))
print()
# Funcion degrees, devuelve el valor en grados del angulo pasado en parametro.
print("degrees - valor en grados del Angulo 1.57: ", math.degrees(1.57))
print()
# Funcion radians, devuelve el valor en radianes del angulo pasado en parametro.
print("cos - Radianes del angulo 90: ", math.radians(90))
print()


