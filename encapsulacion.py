'''Defino una clase con atributos publicos'''
class PuntoPublico:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

'''Defino una claase con atributos privados'''
class PuntoPrivado:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    '''Creo los metodos Get y los Set. 
Los Get recuperan informacion
Los Set setean informacion'''
    def GetX(self):
        return self.__X

    def GetY(self):
        return self.__Y

    def SetX(self, x):
        self.__X = x

    def SetY(self, y):
        self.__Y = y
        
'''Creamos los objetos'''
publico = PuntoPublico(4, 6)
privado = PuntoPrivado(5, 7)

'''Leemos los valores, vemos que los publicos podemos llamarlos directamente.
A los privados no podemos llamarlos directamente, tenemos que llamar al metodo Get
que está dentro de la clase privada'''
print(f"Valores punto privado {publico.X}, {publico.Y}")
print(f"Valores punto privado {privado.GetX()}, {privado.GetY()}")

'''Ahora cambiaremos los parametros de los puntos X.
Como antes, veremos que a los que estan en la clase publica podemos cambiarlos directamente
pero a los de la clase privado solo podemos cambiarlos si usamos el metodo Set de la clase privada
y debemos pasarle el nuevo valor como parametro del metodo'''
publico.X = 15
privado.SetX(42)
'''Volvemos a leer los valore para comprobar que hemos podido cambiar los valores.'''
print(f"Valores punto privado {publico.X}, {publico.Y}")
print(f"Valores punto privado {privado.GetX()}, {privado.GetY()}")

