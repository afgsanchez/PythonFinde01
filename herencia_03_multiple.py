class Hotel:
    def __init__(self):
        self.__NumeroHabitaciones = 0
        self.__Estrellas = 0

    def SetNumeroHabitaciones(self, habs):
        self.__NumeroHabitaciones = habs

    def SetEstrellas(self, estrellas):
        self.__Estrellas = estrellas

    def MostrarHotel(self):
        print("-------------------")
        print("Hotel:")
        print("Estrellas: ", self.__Estrellas)
        print("Nº de Habitaciones: ", self.__NumeroHabitaciones)
        print("-------------------")

class Restaurante:
    def __init__(self):
        self.__Tenedores = 0
        self.__HoraApertura = 0

    def SetTenedores(self, tenedores):
        self.__Tenedores = tenedores

    def SetHoraApertura(self, hora):
        self.__HoraApertura = hora

    def MostrarRestaurante(self):
        print("-------------------")
        print("Restaurante:")
        print("Tenedores: ", self.__Tenedores)
        print("Horario de Apertura: ".upper(), self.__HoraApertura)
        print("-------------------")

class Negocio(Hotel, Restaurante):
    def __init__(self):
        self.__Nombre = ""
        self.__Direccion = ""
        self.__Telefono = 0

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetDireccion(self, direccion):
        self.__Direccion = direccion

    def SetTelefono(self, telefono):
        self.__Telefono = telefono

    def MostrarNegocio(self):
        print("####################")
        print("Negocio: ")
        print("Nombre: ", self.__Nombre)
        print("Direccion: ", self.__Direccion)
        print("Telefono: ", self.__Telefono)
        self.MostrarHotel()
        self.MostrarRestaurante()
        print("####################")

negocio = Negocio()
negocio.SetNombre("Hotel El Rastro")
negocio.SetDireccion("Calle Falsa, 123 - 07620, Llucmajor")
negocio.SetTelefono("+34 123 456 789")
negocio.SetEstrellas("*****")
negocio.SetNumeroHabitaciones(85)
negocio.SetTenedores(4)
negocio.SetHoraApertura("08:00 - 21:00")

negocio.MostrarNegocio()

    
