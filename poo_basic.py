
'''Creamos la clase Persona'''
class Persona():

    '''Asignamos los atributos, que no son más que variables, de la 
    clase Persona, a edad le asignamos un valor de 0, pero al nombre
    lo dejamos en blanco, cada vez que llamemos a Persona nos 
    pedira estos atributos.'''
    edad = 0
    nombre = ""
    altura = 0

    '''Creo el contructor que va a inicializar los atributos.'''
    def __init__(self, nombre, edad, altura):
        
        '''Le damos un valor inicial a los atributos, que serán los
        que recibamos de las variables'''
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    ''' Creamos un metodo que es una funcion que nos devuelve los 
    atibutos edad y nombre y los concatenamos, el atributo edad lo
    convertimos a string para concatenarlo cono texto.
    El argumento self nos indica que puede acceder a los atributos
    de la clase en la que se encuentra el metodo'''
    def leer_edad(self):
        return self.nombre + " tiene " + str(self.edad) + " años.\n" + self.nombre + " mide " + str(self.altura)
    

'''Creamos un objeto (instancia) de la clase Persona, basicamente
consiste en crear una variable a la que le asignamos como valor
la clase Persona, al objeto lo llamaremos jesus por ejemplo.
Ademas, como parámetros le ponemos el nombre Jesus y la edad ya que 
nos lo pide el constructor de la clase 
<< def __init__(self, nombre, edad): >>'''
jesus = Persona("Jesus", 48, 1.86)

'''Ahora vanos a ejecutar una funcion para el objeto jesus.
Vamos a decirle al objeto que ejecute el metodo leer_edad que nos 
devolverá el atributo edad y nombre de su objeto, lo imprimiremos 
en pantalla'''
print(jesus.leer_edad())

'''Ahora para comprobar la reutilizacion de codigo, creo otro objeto
de la clase persona. Gracias a que estamos usando objetos ya no hay 
que escribir todo el codigo de nuevo para el nuevo objeto.
Basta con crear el objeto y llamar a la funcion que queramos ejecutar'''

pepe = Persona("Pepe", 53, 1.78)
print(pepe.leer_edad())


    
