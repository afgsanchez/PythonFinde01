"""# Creamos una clase Pila(), que será basicamente una lista, en un principio vacía.
# La usaremos para cambiar el orden de la cola.
class Pila:

    # Iniciamos el contructor de objetos (en este caso listas)
    def __init__(self):
        # Creamos un atributo (variable) privado (accesible solo dentro de la clase) para la clase Pila.
        # En este caso le asignamos una lista vacía  al atributo.
        self.__items = []

    # Creamos un método (función) que comprobará si la lista self.__items esta vacía.
    # En caso de que esté vacía nos devolverá True, en caso contrario nos devolverá False.
    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    # Creamos un método que añadirá un item a la lista. El ítem que añadirá será
    # el que le pongamos como argumento entre paréntesis al llamar a la función.
    # Para ello usará el método .append() 
    def Apilar(self, item):
        self.__items.append(item)

    # Creamos un método que nos eliminará y devolverá el ultimo ítem de la pila.
    def Retirar(self):
        return self.__items.pop()
    
    # Ahora creamos la clase Cola()
class Cola:
    
    # Iniciamos el constructor, tendrá como atributo una lista vacía.
    def __init__(self):
        self.__items = []

    # Creamos el método para verificar si la cola está vacía.
    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    # Creamos un método que nos va a insertar en la posición 0 de la lista el ítem
    # que le pasemos por parámetro al llamar a este método.
    def Encolar(self, item):
        self.__items.insert(0, item)

    # Creamos un método que nos va a sacar de la ultima posición el ítem
    # que esté en esa posición de las lista al llamar a este método.
    # Para ello simplemente usamos el metodo .pop() que lo que hace es
    # eliminar el último item de la lista y devolver el ítem que ha eliminado.
    def Desencolar(self):
        return self.__items.pop()
    
    # Ahora creamos un método que nos imprimirá en pantalla el cotenido de la cola (lista)
    def MostrarCola(self):
        print(f"Contenido de la cola {self.__items} <-- Primer elemento")


# Ahora creamos el objeto de la clase Cola()
cola = Cola()

# Creamos un bucle for que nos insertará un rango de items (del 0 al 9) en la lista de la Cola()
for i in range(10):
    cola.Encolar(i)
# Llamamos al método MostrarCola() para imprimir en pantalla la cola actual.
cola.MostrarCola()

# Creamos un objeto de la clase Pila, que utilizaremos para darle la vuelta a la lista de la cola.
pila = Pila()

# Creamos un bucle while que mientras que la lista del objeto cola no esté vacia
# irá sacando elementos de la lista, en cada iteración sacará el último elemento de la 
# lista del objeto cola. Esto lo hará llamando a la función EstaVacia() del objeto cola.
# El item que saca lo irá apilando en la lista del objeto pila. Lo hará usando el
# método Apilar() del objeto pila y recibirá el item al usar como parametro el método
# Desencolar() del objeto cola.
while not(cola.EstaVacia()):
    pila.Apilar(cola.Desencolar())

# Ahora creamos otro bucle while que mientras que la lista del objeto pila no esté vacía
# irá insertando items en la lista del objeto cola. Para ello usará el método Encolar() del
# objeto cola y como parámetro tendrá en método Retirar() del objeto pila.
while not(pila.EstaVacia()):
    cola.Encolar(pila.Retirar())

# Ahora llamamos al método MostrarCola() del objeto cola.
cola.MostrarCola()"""

#################################################################################################

# Creamos la clase Cola()
class Cola:
    
    # Iniciamos el constructor, tendrá como atributo una lista vacía.
    def __init__(self):
        self.__items = []

    # Creamos el método para verificar si la cola está vacía.
    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    # Creamos un método que nos va a insertar en la posición 0 de la lista el ítem
    # que le pasemos por parámetro al llamar a este método.
    def Encolar(self, item):
        self.__items.insert(0, item)

    # Creamos un método que nos va a sacar de la ultima posición el ítem
    # que esté en esa posición de las lista al llamar a este método.
    # Para ello simplemente usamos el metodo .pop() que lo que hace es
    # eliminar el último item de la lista y devolver el ítem que ha eliminado.
    def Desencolar(self):
        return self.__items.pop()
    
    def LeerPrimerElemento(self):
        return self.__items[len(self.__items)-1]
    
    def LeerUltimoElemento(self):
        colaauxiliar = Cola()
        while not (self.EstaVacia()):
            ultimoelemento = self.Desencolar()
            colaauxiliar.Encolar(ultimoelemento)
        while not (colaauxiliar.EstaVacia()):
            self.Encolar(colaauxiliar.Desencolar())
        return ultimoelemento
    
    def NumeroElementos(self):
        colaauxiliar = Cola()
        numeroelementos = 0
        while not (self.EstaVacia()):
            numeroelementos += 1
            colaauxiliar.Encolar(self.Desencolar())
        while not (colaauxiliar.EstaVacia()):
            self.Encolar(colaauxiliar.Desencolar())
        return numeroelementos
    
    # Ahora creamos un método que nos imprimirá en pantalla el cotenido de la cola (lista)
    def MostrarCola(self):
        print(f"Contenido de la cola {self.__items} <-- Primer elemento")

# Ahora, fuera de la clase Cola:

def SimuladorCola():
    fin = False
    cola = Cola()

    while not (fin):
        opc = input("Opción: ")
        match opc:
            case "1":
                item = input("Elemento a Encolar: ")
                cola.Encolar(item)
                print(f"Elemento Encolado {item}")
            case "2":
                if cola.EstaVacia():
                    print("La cola está vacia, no se puede desencolar nada.")
                else:
                    item = cola.LeerPrimerElemento()
                    cola.Desencolar()
                    print(f"Elemento Desencolado {item}")
            case "3":
                if cola.EstaVacia():
                    print("La cola esta vacía, no puede leerse nada.")
                else:
                    print(f"El Primer Elemento de la cola es: {cola.LeerPrimerElemento()} ")
            case "4":
                if cola.EstaVacia():
                    print("La cola esta vacía, no puede leerse nada.")
                else:
                    print(f"El Ultimo Elemento de la cola es: {cola.LeerUltimoElemento()}")
            case "5":
                if cola.EstaVacia():
                    print("La cola está vacia.")
                else:
                    print("La cola no está vacía.")
            case "6":
                print(f"Numero de Elementos: {cola.NumeroElementos()}")
            case "7":
                cola.MostrarCola()
            case "8":
                fin = True

print("""************
      SIMULADOR DE COLA
      ************
      --- MENU ---
      1. Encolar
      2. Desencolar
      3. Leer Primer Elemento
      4. Leer Ultimo Elemento
      5. ¿Está Vacía?
      6. Numero de Elementos
      7. Mostrar Cola
      8. Fin""")

SimuladorCola()

