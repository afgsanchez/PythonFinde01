'''Igual que en las variables privadas, para definir un metodo privado debemos 
incluir dos guines bajos "__" delante del nombre.
En este ejemplo crearemos dos metodos privados y uno publico mediante el cual
uyilizaremos los dos privados.'''

# Creamos la clase
class OperarValores:
    def __init__(self, v1, v2):
        self.__V1 = v1
        self.__V2 = v2

    # Creamos los dos metodos privados __Sumar y __Restar
    def __Sumar(self):
        return self.__V1 + self.__V2
    
    def __Restar(self):
        return self.__V1 - self.__V2
    
    # Ahora creamos el metodo publico desde el cual utilizaremos los privados
    def Operar(self):
        print(f"La suma es: {self.__Sumar()}\n")
        print(f"La resta es: {self.__Restar()}\n")

# Ahora creamos el objeto y le damos los parametros (los numeros a operar)
operarvalores = OperarValores(4, 6)

# Y ahora llamamos al metodo publico Operar el cual llamará a su vez a los privados
# y estos nos devolveran los resultados de las operaciones.
operarvalores.Operar()

