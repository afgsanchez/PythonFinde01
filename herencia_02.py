'''Para ver la herencia, crearemos una clase principal (padre) y luego una clase hijo que
heredará los atributos y metodos de la clase padre pero ademas tendrá los suyos propios.
Para crear una clase hijo, en la definicion de la clase solo debemos ponerle como parametro
el nombre de la clase padre'''

#Creamos la clase padre
class Electrodomestico:
    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0

    def Encender(self):
        self.__Encendido = True

    def Apagar(self):
        self.__Encendido = False

    def Encendido(self):
        return self.__Encendido
    
    def SetTension(self, tension):
        self.__Tension = tension

    def GetTension(self):
        return self.__Tension
    
# Ahora creamos la clase hijo
class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0

    def SetRPM(self, rpm):
        self.__RPM = rpm

    def SetKilos(self, kilos):
        self.__Kilos = kilos

    def MostrarLavadora(self):
        print("\n########################")
        print("Lavadora")
        print("\tRPM: ", self.__RPM)
        print("\tKilos: ", self.__Kilos)
        print("\tTension: ", self.GetTension())

        if self.Encendido():
            print("\tLavadora encendida!")
        else:
            print("\tLavadora apagada!")
        print("########################\n")

class Microondas(Electrodomestico):
    def __init__(self):
        self.__PotenciaMaxima = 0
        self.__Grill = False

    def SetPotenciaMaxima(self, potencia):
        self.__PotenciaMaxima = potencia

    def SetGrill(self, grill):
        self.__Grill = grill

    def MostrarMicroondas(self):
        print("\n########################")
        print("Microondas")
        print("\tPotencia Maxima: ", self.__PotenciaMaxima)
       
        if self.__Grill == True:
            print("\tGrill: Sí")
        else:
            print("\tGrill: No")
        print("\tTension: ", self.GetTension())

        if self.Encendido():
            print("\tMicroondas encendido.")
        else:
            print("\tMicroondas apagado.")
        print("########################\n")


# Creamos el objeto lavadora
lavadora = Lavadora()
# Asignamos parametros
lavadora.SetRPM(1200)
lavadora.SetKilos(8)
lavadora.SetTension(230)
lavadora.Encender()

# Creamos el objeto microondas
microondas = Microondas()
# Asignamos parametros
microondas.SetPotenciaMaxima(650)
microondas.SetGrill(True)
microondas.SetTension(230)
microondas.Apagar()

lavadora.MostrarLavadora()
microondas.MostrarMicroondas()

