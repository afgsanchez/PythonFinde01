''' Como trabajar con archivos.
Crear, abrir, leer, grabar y cerrar archivos de texto'''

#Ejemplo 1
'''En este ejemplo vamos a crear un archivo desde el codigo, lo abrimos en modo "x" para crearlo 
y poder escribir en el directamente'''
# Creamos y abrimos abrimos el archivo
fcrear = open("nuevoarchivo.txt", "x")
# Escribimos un par de lineas de muestra con un solo comando.
fcrear.write("LINEA 1\nLINEA 2\nLINEA 3\n") # -> Terminamos con \n para que haga un salto de linea
# Añadimos otra linea repitiendo en comando anterior
fcrear.write("LINEA 4")
# Cerramos el archivo
fcrear.close()

'''Vamos a abrirlo y leerlo para comprobar que ha ido bien'''
f =open("nuevoarchivo.txt", "r")
texto = f.read()
f.close()
print(texto)



