# La libreria multiprocessing contiene todo lo necesario para trabajar con procesos.

# La sintaxis es similar a la de los hilos.
'''
variable = multiprocessing.Process(target=NombreFuncion())

Hay que iniciarlo:
variable.start()

Se puede usar tambien el metodo join para que espere a cerrar el programa a que los procesos hayan terminado
variable.join()

'''
# Veamos unos ejemplos.
import os
import time
import threading
import multiprocessing

def MostrarInformacion():
    print("PID: %s, Nombre proceso: %s"%(os.getpid(), multiprocessing.current_process().name))
    print()

if __name__=='__main__':
    MostrarInformacion()
    proceso1 = multiprocessing.Process(target=MostrarInformacion)
    proceso2 = multiprocessing.Process(target=MostrarInformacion)
    proceso3 = multiprocessing.Process(target=MostrarInformacion)
    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso1.join()
    proceso2.join()
    proceso3.join()
