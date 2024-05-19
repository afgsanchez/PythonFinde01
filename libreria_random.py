# La libreria random nos permite hafer elecciones aleatorias, elegir al azar 
# un valor de una lista, generar nuemro aleatorios y obtener un numero al azar dentro de un rango.

# Tenemos que importar la libreria random
import random
print()
#Funcion randrange, devuelve u numero aleatorio en un rango especificado en parametro.
print("Numero aleatorio en el rango 1-100: ", random.randrange(100))
print()
# Funcion sample, devuelve una lista de de numeros aleatorio en un rango especificado por parametro.
# Hay dos parametros, el primero establece el rango y el segundo la cantidad de elementos de la lista que queremos.
print("LIsta aleatoria de 6 numeros en el rango 1-100", random.sample(range(100),6))
print()
# Funcion random, devuelve un numero en coma flotante (decimales)
print("Numero float aleatorio: ", random.random())
print()
# Funcion choice, selecciona un elemento al azar de una lista que recibe por parametro.
print("Eleccion de un elemento de forma aleatoria de la siguiente lista: ['rojo', 'verde', 'azul', 'amarillo']", random.choice(['rojo', 'verde', 'azul', 'amarillo']))
print()
