# Esta libreria nos permitirá interactuar con el sistema operativo y 
# manejar funcionalidades.

# Lo primero es importar la libreria os
import os

print()

# Funcion getcwd, devuelve el directorio actual de trabajo de la aplicacion
print("getcwd - El directorio actual es: ", os.getcwd())
print()

# Funcion chdir, cambia al directorio que le indiquemos por patrametro.
# Para ver el nuevo directorio de trabajo debemos usar la funcion getcwd
os.chdir("/Users/afgsa/Desktop/Curso Python IBM/MasterClass/")
print("chdir - Nuevo directorio de trabajo: ", os.getcwd())
print()

# Funcion getpid, nos devuelve el identificador del proceso del aplicativo
print("getpid - El identificador del proceso del aplicativo es: ", os.getpid())
print()

# Funcion getuid, nos devuelve el identificador del usuario del proceso del aplicativo
# ATENCION ESTE NO FUNCIONA EN ENTORNOS WINDOWS
# print("getuid - El identificado del usuario es: ", os.getuid())

# Para Windows podemos usar la libreria getpass y su funcion getuser
import getpass
print("getuid - El identificado del usuario es: ", getpass.getuser())

# Funcion listdir, devuelve una lista del contenido del directorio actual de trabajo.
print("listdir - El contenido del directorio es: ", os.listdir())
print()

# Funcion mkdir, crea un nuevo directorio dentro del directorio actual de trabajo
try:
    print("mkdir - Creando el directorio 'PRUEBAS", os.mkdir("PRUEBAS"))
except:
    print("Error")
print(os.listdir())
print()


