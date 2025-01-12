#Programa para calcular el area de diferentes figuras geométricas

#Importamos la librearía "math" para poder calcular pi
import math

#Clase para determinar las figuras
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiene_dimension = False

    def area(self):
        pass

#Clase para determinar área del Rectángulo
class Rectangulo(Figura):
    def __init__(self, base, altura, es_valido=True):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
        self.tiene_dimension = es_valido

    def area_del_rectangulo(self):
        if self.tiene_dimension:
            return self.base * self.altura
        else:
            return "Dimesniones inválidas para realizar cualquier cálculo"

#Clase para determinar área de círculo
class Circulo(Figura):
    def __init__(self, radio, es_valido=True):
        super().__init__("Círculo")
        self.radio = radio
        self.tiene_dimension = es_valido

    def area_del_circulo(self):
        if self.tiene_dimension:
            return round(math.pi * self.radio ** 2, 2)
        else:
            return "Dimesniones inválidas para realizar cualquier cálculo"

#Clase para determinar área del triángulo
class Triangulo(Figura):
    def __init__(self, base, altura, es_valido=True):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura
        self.tiene_dimension = es_valido

    def area_de_triangulo(self):
        if self.tiene_dimension:
            return (self.base * self.altura)/2
        else:
            return "Dimensiones inválidas para realizar cálculo"

#Creamos instancias
def main():
    rectangulo = Rectangulo(12, 8, True)
    circulo = Circulo(5, True)
    triangulo = Triangulo(4, 7, False)

    print(f"El área del {rectangulo.nombre} es igual a {rectangulo.area_del_rectangulo()} unidades cuadradas")
    print(f"El área del {circulo.nombre} es igual a {circulo.area_del_circulo()} unidades cuadradas")
    print(f"EL área del {triangulo.nombre} es igual a {triangulo.area_de_triangulo()} unidades cuadradas")

if __name__ == "__main__":
    main()








