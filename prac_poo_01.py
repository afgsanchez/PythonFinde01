# Practicas con Clases y POO

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

# Ahora creo un objeto (instancia) de la clase Punto y le asigno los valores
# a los atributos x, y
p1 = Punto(5,7)

# Ahora llamo a la funcion mostrar_punto del objeto p1 que me debe ejecutar el metodo
# con los valores que le hemos pasado al objeto.
p1.mostrar_punto()


    
    
