''' Como trabajar con archivos.
Abrir, leer, grabar y cerrar archivos de texto'''

# Ejemplo 1
'''Abrimos el archivo prueba.txt que esta en el mismo directorio que el programa,
lo leemos con read y lo cargamos en una variable del tipo string. Luego lo mostramos
en pantalla con un print de la variable.'''
# Abrimos el archivo en modo lectura "r"
f = open("prueba.txt", "r")
# leemos en archivo y lo guardamos en la variable texto
texto = f.read()
# imprimimos la variable en pantalla
print(texto)
# cerramos el archivo
f.close

# Ejemplo 2
'''Usamos un bucle for para que nos lea una linea en cada iteracion'''
f = open("prueba.txt", "r")
for linea in f:
    print(linea)
f.close()

# Ejemplo 3
'''En este ejemplo vamos a usar el comando readline para leer una linea, luego
imprimimos solo el numero de lineas que queramos'''
f = open("prueba.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# Ejemplo 4 
'''Aqui convertiremos cada linea en un elemento de una lista con el comando readlines()
Luego podemos imprimir las linesa que nos interesen indicando el numero de elemento en la lista
y en el orden que queramos'''
f = open("prueba.txt", "r")
lineas = f.readlines()
f.close
print(lineas[1])
print(lineas[0])

# Ejemplo 5
'''Hacemos algo parecido al anterior, o sea, guardamos las lineas como elementos de una lista.
Luego recorremos la lista con un bucle for y lo imprimimos'''
f = open("prueba.txt", "r")
lineas = list(f)
f.close()
for item in lineas:
    print(item)
