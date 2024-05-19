# Practicas con Clases y POO - 3
#MOdificar informacion almacenada en una clase

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

# Ahora creo el objeto (instancia) de la clase Punto y le asigno los valores
# a los atributos x, y
p1 = Punto(5,7)

# Ahora llamo a la funcion mostrar_punto de los objetos que me deben ejecutar el metodo
# con los valores que le hemos pasado a los objetos.
p1.mostrar_punto()

# Ahora vamos a modificar el valor de x. Para ello variamos el atributo (variable) x del
# objeto p1. Luego volvemos a llamara al metodo para ver la diferencia.
p1.X = 25
p1.mostrar_punto()


