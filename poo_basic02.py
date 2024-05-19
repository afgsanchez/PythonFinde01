class Rectangulo:
    ancho = 0
    altura = 0

    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura

ancho = int(input("Pon el ancho del r1: "))
altura = int(input("Pon la altura del r1: "))

rectangulo1 = Rectangulo(ancho,altura)
print(f"El area del rectangulo es: {rectangulo1.area()}")

ancho = int(input("Pon el ancho del r2: "))
altura = int(input("Pon la altura del r2: "))

rectangulo2 = Rectangulo(ancho,altura)
print(f"El area del rectangulo es: {rectangulo2.area()}")
    
