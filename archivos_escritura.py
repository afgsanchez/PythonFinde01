''' Como trabajar con archivos.
Crear, abrir, leer, grabar y cerrar archivos de texto'''

# Ejemplo 1
'''Añadir lineas al archivo de texto conservando el contenido original
Para eelo usaremos el argumento "a" para abrir el archivo en modo añadir escritura 
y el comando .write para escribir en el archivo'''
# Abrimos el archivo en modo "a" append
fescritura = open("prueba.txt", "a")
# Con el comando .escritura grabamos la nueva linea al archivo
fescritura.write("LINEA 4 - Esta linea esta añadida desde codigo")
# Cerramos el archivo
fescritura.close()


