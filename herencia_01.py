'''Para ver la herencia, crearemos una clase principal (padre) y luego una clase hijo que
heredará los atributos y metodos de la clase padre pero ademas tendrá los suyos propios.
Para crear una clase hijo, en la definicion de la clase solo debemos ponerle como parametro
el nombre de la clase padre'''

#Creamos la clase padre
class Electromestico:
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
class Lavadora(Electromestico):
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

# Creamos el objeto
lavadora = Lavadora()
lavadora.SetRPM(0)
lavadora.SetKilos(8)
lavadora.SetTension(230)
lavadora.Apagar()
lavadora.MostrarLavadora()

fin = False
while not (fin):
    
    estado = input("¿Quieres encender o apagar la lavadora?\nPulsa 'e' para encender.\nPulsa 'a' para apagar.\nPulsa s para salir: ")
    if estado == "e":
        lavadora.SetRPM(800)
        lavadora.Encender()
    elif estado =="a":
        lavadora.SetRPM(0)
        lavadora.Apagar()
    elif estado == "s":
        fin = True
    else:
        print("Elige y/n")
    lavadora.MostrarLavadora()

