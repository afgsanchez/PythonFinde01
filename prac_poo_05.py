# Practicas con Clases y POO - 5
# COMPOSICION - Utilizar clases como atributos de otras clases
'''Crearemos tres objetos de la clase Punto y un objeto de la clase Triangulo que
recibira los tres objetos de la clase Punto como parametro'''

# Creo la clase del tipo Punto (para coordenadas por ejemplo)
class Punto:

    # Inicio el constructor y le asigno los atributos (lo que es, en realidad
    # son variables) x, y
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # Ahora creamos un metodo (lo que puede hacer)
    def mostrar_punto(self):
        # print("El punto es (",self.X,",",self.Y,")")
        print(f"El punto es {self.X},{self.Y}")

# Creo la clase del tipo Triangulo que tiene tres atributos (v1, v2, v3) que recibira
# los valores de los objetos la clase Punto.
class Triangulo:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3

    # Creamos un metodo para la clase Triangulo
    def mostrar_vertices(self):
        self.V1.mostrar_punto()
        self.V2.mostrar_punto()
        self.V3.mostrar_punto()
        


# Ahora creo tres objetos (instancia) de la clase Punto y le asigno los
# valores a los attributos x, y
v1 = Punto(5,7)
v2 = Punto(3,6)
v3 = Punto(4,7)

# Ahora creo eun objeto de la clase Triangulo() y como valores le asigno los objetos
# que hemos cfeado de la clase Punto()
triangulo = Triangulo(v1,v2,v3)

# Ahora llamamos al metodo que hemos creado para la clase Triangulo para usarlo con el objeto
triangulo.mostrar_vertices()




