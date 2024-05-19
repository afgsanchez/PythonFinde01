class Pila():
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
        
    def Apilar(self, item):
        self.__items.append(item)

    def Retirar(self):
        return self.__items.pop()
    
    def LeerCima(self):
        return self.__items [len(self.__items) -1]
    
    def MostrarPila(self):
        print("Pila: ", self.__items, "<-- CIMA")

    def LeerFondo(self):
        pilaauxiliar = Pila()
        while not(self.EstaVacia()):
            pilaauxiliar.Apilar(self.Retirar())
        valorfondo = pilaauxiliar.LeerCima()
        while not(pilaauxiliar.EstaVacia()):
            self.Apilar(pilaauxiliar.Retirar())
        return valorfondo
    def NumeroElementos(self):
        pilaauxiliar = Pila()
        while not(self.EstaVacia()):
            pilaauxiliar.Apilar(self.Retirar())
        numeroelementos = 0
        while not(pilaauxiliar.EstaVacia()):
            self.Apilar(pilaauxiliar.Retirar())
            numeroelementos += 1
        return numeroelementos
        

def SimuladorPila():
    fin = False
    pila = Pila()
    
    while not(fin):
        
        opc = input("Opcion: ")
        if opc == "1":
            item = input("Introduzca elemento a apilar: ")
            pila.Apilar(item)
            print("Elemento apilado: ", item)
        elif opc == "2":
            if pila.EstaVacia():
                print("la pila está vacia, no se puede retirar ningun elemento.")
            else:
                item = pila.LeerCima()
                pila.Retirar()
                print("Elemento retirado: ", item)
        elif opc == "3":
            if pila.EstaVacia():
                print("La pila esta vacia no se puede leer la CIMA.")
            else:
                print("La Cima de la pila es: ", pila.LeerCima())
        elif opc == "4":
            if pila.EstaVacia():
                print("La pila esta vacia.")
            else:
                print("La pila no esta vacia")
        elif opc == "5":
           pila.MostrarPila()
        elif opc == "6":
            if pila.EstaVacia():
                print("La pila esta vacia no se puede leer el FONDO.")
            else:
                print("El Fondo de la pila es: ", pila.LeerFondo())
        elif opc == "7":
            print(pila.NumeroElementos())  
        elif opc == "8":
            print("Adios!")
            fin = True


print("""*****************
      Simulador de Pila
      ******************
      Menu:
      1. Apilar
      2. Retirar
      3. Leer Cima
      4. ¿Está Vacía?
      5. Mostrar Pila
      6. Leer Fondo
      7. Número de elementos
      8. Salir
      """)
SimuladorPila()
         

