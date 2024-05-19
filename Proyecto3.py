# Tercer Proyecto del libro APRENDE PYTHON EN UN FIN DE SEMANA
'''PROYECTO 3 - BIBLIOTECA'''
# Empezamos
''' Definimos tres clases, Autor, Libro, Biblioteca'''

# Clase Autor, con atributos nombre y apellidos
class Autor:
    def __init__(self, Nombre, Apellidos):
        self.Nombre = Nombre
        self.Apellidos = Apellidos

    ''' Creamos el metodo MostrarAutor, que mostrará los atributos Nombre y Apellidos'''
 
    def MostrarAutor(self):
        print(f"El autor es {self.Nombre} {self.Apellidos}")

# Clase Libro, con atributos Titulo, ISBN
class Libro:
    def __init__(self, Titulo, ISBN):
        self.Titulo = Titulo
        self.ISBN = ISBN
        self.Autor = None

    ''' Creamos tres metodos, AñadirAutor, MostrarLibro, ObtenerTitulo'''

    def AñadirAutor(self, autor):
        self.Autor = autor

    def MostrarLibro(self):
        print("---Libro---")
        print("Titulo: ",self.Titulo)
        print("ISBN: ",self.ISBN)
        if self.Autor:
            self.Autor.MostrarAutor()
        else:
            print("Autor no asignado")
        print("-----------")
        
    def ObtenerTitulo(self):
        return self.Titulo;
        
    
# Clase Biblioteca, con atributos ListaLibros
class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    ''' Creamos los metodos:
NumeroLibros que devuelve el numero de libros de la libreria
AñadirLibro que almacena el libro pasado por parametro en la lista de libros que tiene como atributo
BorrarLibro que elimina un libro de la biblioteca a oartir de su titulo
MostrarBiblioteca muestra todos los libros de la biblioteca'''

    def NumeroLibros(self):
        return len(self.ListaLibros)

    def AñadirLibro(self, libro):
        self.ListaLibros = self.ListaLibros + [libro]

    def BorrarLibro(self, titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionaborrar]
            print("Libro borrado!")
        else:
            print("Libro no encontrado.")

    def MostrarBiblioteca(self):
        print("###############################")
        for item in self.ListaLibros:
            item.MostrarLibro()
        print("###############################")

# Ahora añadiremos un menu de funciones.
def MostrarMenu():
    print("**************")
    print("* BIBLIOTECA *")
    print("**************")
    print("""Menu:\n
1. Añadir Libro a la Biblioteca
2. Mostrar Biblioteca
3. Borrar Libro
4. Numero de Libros
5. Salir""")

# Añadimos la funcion de añadir un libro:
def AñadirLibroABiblioteca(biblioteca):
    titulo = input("Introduzca el titulo del libro: ")
    isbn = input("Introduzca el ISBN: ")
    autornombre = input("Introduzca el nombre del autor: ")
    autorapellidos = input("Introduzca los apellidos del autor: ")
    autor = Autor(autornombre, autorapellidos)
    libro = Libro(titulo, isbn)
    libro.AñadirAutor(autor)
    biblioteca.AñadirLibro(libro)
    return biblioteca

def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibro(biblioteca):
    titulo = input("Introduzca el titulo del libro a borrar: ")
    biblioteca.BorrarLibro(titulo)

def NumeroLibros(biblioteca):
    print("En la biblioteca hay ",biblioteca.NumeroLibros(), " libros")

# Añadimos el bucle para que el programa funcione constantemente hasta que salgamos.
fin = False
biblioteca = Biblioteca()

while not(fin):
    try:
        MostrarMenu()
        opcion = int(input("Elige una opcion: "))

        match opcion:
            case 1:
                biblioteca = AñadirLibroABiblioteca(biblioteca)
                
            case 2:
                MostrarBiblioteca(biblioteca)
                
            case 3:
                BorrarLibro(biblioteca)

            case 4:
                NumeroLibros(biblioteca)

            case 5:
                print("Gracias por usar la Biblioteca")
                fin = True

    except ValueError:
        print("Elige una opcion del 1 al 5 por favor.")
