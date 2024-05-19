# Practicas con Clases y POO - 4
# Asignando objetos, se asignan los valores que tiene el objeto en sus atributos.

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

# Creo otro objeto de la clase Punto
p2 = Punto(22,33)

# Llamamos al metodo mostrar_punto
p2.mostrar_punto()

# Ahora le asignamos los valores de p2 a p1 y llamamos al metodo mostrar_punto
# para ver como p1 toma los valores de p2
p1 = p2
p1.mostrar_punto()
