print()
print("""Para crear el hilo se utiliza la siguiente sintaxis:
variable = threading.Thread(target=NombreFuncion)

El siguiente paso es inicializarlo:
variable.start()

Funcionalidad que detiene le programa hastq eu el hilo termina de ejecutarse:
variable.join()

Obtener el nombre del hilo en ejecucion:
threading.current_thread().name
¡¡ OJO !! EN VERSIONES ANTERIORES DE PYTHON EN LUGAR DE USAR .name SE USABA .getName()

Obtener el identificador del hilo en ejecucion:
threadin.current_thread().ident

""")

# Ejercicio01 - Crear, ejecutar hilos. Diferencia en ejecucion de la funcion con hilos y sin hilos.

# Iportamos la libreria threading que es la que nos permite trabajar con hilos.
import threading
import time # Usaremos tambien esta libreria para hacer los ejemplos.

# Creamos una funcion que mostrará la informacion del hilo que se está ejecutando.
def MostrarInformacion():
    print("Hilo: ", threading.current_thread().name, "con identificador:", threading.current_thread().ident)
print()
# Ahora llamamos a la funcion varias veces sin usar hilos para ver su comportamiento en modo secuencial.
print("# Ejecución sin hilos #")
MostrarInformacion()
MostrarInformacion()
MostrarInformacion()
MostrarInformacion()
print("\n")

# Ahora usamos hilos
print("# Ejecución con hilos #")
hilo1 = threading.Thread(target=MostrarInformacion)
hilo2 = threading.Thread(target=MostrarInformacion)
hilo3 = threading.Thread(target=MostrarInformacion)
hilo4 = threading.Thread(target=MostrarInformacion)
#Iniciamos los hilos y les añadimos un retardo de 1 segundo para apreciarlo mejor. El retardo es opcional
hilo1.start()
time.sleep(1)
hilo2.start()
time.sleep(1)
hilo3.start()
time.sleep(1)
hilo4.start()
time.sleep(1)
# Usamos el metodo join para que el programa no acabe hasta que terminen todos los hilos.
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
print()

# Ejercicio02, hacemos lo mismo que en el anterior ejercicio pero en esta ocasion le daremos nosotros 
# el nombre a los hilos.

# Creamos los hilos con un nombre que le proporcionamos nosotros en el parametro.
print("# Ejecución con hilos con NOMBRE#")
hilo1 = threading.Thread(name = "hilo 01", target=MostrarInformacion)
hilo2 = threading.Thread(name = "hilo 02", target=MostrarInformacion)
hilo3 = threading.Thread(name = "hilo 03", target=MostrarInformacion)
hilo4 = threading.Thread(name = "hilo 04", target=MostrarInformacion)
#Iniciamos los hilos y les añadimos un retardo de 1 segundo para apreciarlo mejor. El retardo es opcional
hilo1.start()
time.sleep(1)
hilo2.start()
time.sleep(1)
hilo3.start()
time.sleep(1)
hilo4.start()
time.sleep(1)
# Usamos el metodo join para que el programa no acabe hasta que terminen todos los hilos.
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()
print()


# Ejercicio03 Eliminaremos las sentencias join.
# El programa terminará antes que los hilos que siguen ejecutandose y mostrando info en pantalla.

# Creamos los hilos con un nombre que le proporcionamos nosotros en el parametro.
print("# Ejecución con hilos con NOMBRE sin JOIN#")
hilo1 = threading.Thread(name = "hilo 01", target=MostrarInformacion)
hilo2 = threading.Thread(name = "hilo 02", target=MostrarInformacion)
hilo3 = threading.Thread(name = "hilo 03", target=MostrarInformacion)
hilo4 = threading.Thread(name = "hilo 04", target=MostrarInformacion)
#Iniciamos los hilos y les añadimos un retardo de 1 segundo para apreciarlo mejor. El retardo es opcional
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
print()

# Ejercicio04 Ahora iniciaremos un hilo y hasta que este no termine no iniciaremos el siguiente

# Creamos los hilos con un nombre que le proporcionamos nosotros en el parametro.
print("# Ejecución con hilos con NOMBRE, HASTA QUE NO TERMINE UN HILO NO SE INICIA EL SIGUIENTE #")
hilo1 = threading.Thread(name = "hilo 01", target=MostrarInformacion)
hilo2 = threading.Thread(name = "hilo 02", target=MostrarInformacion)
hilo3 = threading.Thread(name = "hilo 03", target=MostrarInformacion)
hilo4 = threading.Thread(name = "hilo 04", target=MostrarInformacion)
#Iniciamos los hilos y les añadimos un retardo de 1 segundo para apreciarlo mejor. El retardo es opcional
hilo1.start()
hilo1.join()
hilo2.start()
hilo2.join()
hilo3.start()
hilo3.join()
hilo4.start()
hilo4.join()
print()

# Ejercicio05 - Ahora pasaremos parametros a la funcion ejecutada por el hilo.
# Modificaremos la funcion añadiendo dos parametros de entrada.

# Creamos la funcion con dos parametros .
def MostrarInformacion2(num_hilo, **secuencia):
    print("Hilo: ", threading.current_thread().name, "con identificador:", threading.current_thread().ident)

    for valor in range(secuencia['comienzo'],secuencia['fin'], 1):
        print(valor)
print()


# Crearemos los hilos usando un bucle for
print("# Ejecución con hilos y parametros#")

# Creamos una variable para definir el numero de hilos que creará el bucle for
HILOS = 4

for num_hilo in range(HILOS):
    comienzo = num_hilo*10
    fin = 10 + num_hilo*10
    hilo = threading.Thread(target=MostrarInformacion2, args=(num_hilo,), kwargs={'comienzo':comienzo, 'fin':fin})

    hilo.start()
    hilo.join() # Si obviamos esta linea ejecutará todos los hilos a la vez.

print()