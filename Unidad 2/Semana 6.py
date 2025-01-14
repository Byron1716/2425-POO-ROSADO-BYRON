# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Atributo encapsulado
        self.__salario = salario  # Atributo encapsulado

    def mostrar_informacion(self):
        return f"Nombre: {self.__nombre}, Salario: {self.__salario}"

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario(self):
        return self.__salario

    def aumentar_salario(self, porcentaje):
        self.__salario += self.__salario * (porcentaje / 100)


# Clase derivada Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.__lenguaje = lenguaje # Atributo encapsulado

    # Sobrescribir el metodo mostrar_informacion (Polimorfismo)
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Lenguaje de programación: {self.__lenguaje}"


# Clase derivada Diseñador
class Disenador(Empleado):
    def __init__(self, nombre, salario, herramienta):
        super().__init__(nombre, salario)
        self.__herramienta = herramienta  #Atributo encapsulado

    # Sobrescribir el metodo mostrar_informacion (Polimorfismo)
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Herramienta de diseño: {self.__herramienta}"


def main():
    # Crear instancias de cada tipo de empleado
    desarrollador = Desarrollador("Ana Pérez", 50000, "Python")
    disenador = Disenador("Juan Gómez", 45000, "Photoshop")

    # Mostrar información de los empleados
    print(desarrollador.mostrar_informacion())
    print(disenador.mostrar_informacion())

    # Aumentar salario
    desarrollador.aumentar_salario(50)
    disenador.aumentar_salario(25)

    # Mostrar información actualizada
    print("")
    print("\nINFORMACIÓN ACTUALIZADA")
    print(desarrollador.mostrar_informacion())
    print(disenador.mostrar_informacion())


if __name__ == "__main__":
    main()
