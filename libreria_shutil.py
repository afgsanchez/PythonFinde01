# La libreria shutil nos permite trabajar con ficheros.

# Lo primero importamos el modulo.
import shutil
import os

os.chdir("/Users/afgsa/Desktop/Curso Python IBM/MasterClass/")

print()

# Funcion copy, copia un archivo, le decimos origen y nombre de copia por parametros
print("copy - Copiamos el archivo pruebaderenombre.py y a la copia la nombramos pruebacopia.py", shutil.copy("pruebaderenombre.py", "pruebacopia.py"))
print()

# Funcion move, mueve el fichero especificado a la ruta especificada.
print("move - Movemos el archivo pruebaderenombre.py a la ruta C:\\Users\\afgsa\\Desktop\\test", shutil.move("pruebaderenombre.py", "C:/Users/afgsa/Desktop/test/test.py"))
print()

# Funcion rmtree, elimina el directorio especificado y su contenido
print("rmtree - Eliminamos el directorio C://Users//afgsa//Desktop//test//test.py y su contenido.", shutil.rmtree("C:/Users/afgsa/Desktop/test"))
print()


