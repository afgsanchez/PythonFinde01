# Practicas con Clases y POO - 2

# Creo la clase del tipo Punto (para coordenadas por ejemplo)
class Punto:

    # Inicio el constructor y le asigno los atributos (lo que es) x, y
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # Ahora creamos un metodo (lo que puede hacer)
    def mostrar_punto(self):
        # print("El punto es (",self.X,",",self.Y,")")
        print(f"El punto es {self.X},{self.Y}")

# Ahora creo varios objetos (instancias) de la clase Punto y le asigno los valores
# a los atributos x, y
p1 = Punto(5,7)
p2 = Punto(1,6)
p3 = Punto(2,8)
p4 = Punto(9,9)


# Ahora llamo a la funcion mostrar_punto de los objetos que me deben ejecutar el metodo
# con los valores que le hemos pasado a los objetos.
p1.mostrar_punto()
p2.mostrar_punto()
p3.mostrar_punto()
p4.mostrar_punto()
