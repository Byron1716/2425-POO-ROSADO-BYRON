# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Promedio semanal de temperaturas.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print("")
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

#Programación Orientada a Objetos
print("")
class ClimaDiario: #Creamos el nombre de la clase
    #definimos nuestro método constructor con sus respectivos atributos
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura
#Métodos Adicionales (Funciones en programación Tradicional)
    def obtener_temperatura(self):
        return self.temperatura

    def __str__(self):
        return f"Día {self.dia}: {self.temperatura}°C"

#Creamos la clase Clima Semanal con sus respectivos atributos
class ClimaSemanal:
    def __init__(self):
        self.datos_semanales = []
#Métodos para ingresar la temperautra diaria
    def ingresar_temperatura_diaria(self, dia, temperatura):
        clima_diario = ClimaDiario(dia, temperatura)
        self.datos_semanales.append(clima_diario)

# Métodos para calcular el promedio de las temperaturas
    def calcular_promedio_semanal(self):
        if not self.datos_semanales:
            return 0
        total = sum([clima.obtener_temperatura() for clima in self.datos_semanales])
        return total / len(self.datos_semanales)


    def mostrar_datos_semanales(self):
        for clima in self.datos_semanales:
            print(clima)


def main():
    clima_semanal = ClimaSemanal()
# Pedimos los datos al usuario para sacar los promedios
    print("Ingrese las temperaturas diarias para la semana.")
    for dia in range(1, 8):  # 7 días de la semana
        temperatura = float(input(f"Temperatura para el día {dia}: "))
        clima_semanal.ingresar_temperatura_diaria(dia, temperatura)

    clima_semanal.mostrar_datos_semanales()
    promedio = clima_semanal.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()
