#Creamos una clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

#Definimos una función para cargar inventario
    def cargar_inventario(self):
        try:
            with open("Deber Semana 9.txt", "r") as archivo:   #Abrimos el archivo ya existente
                for linea in archivo:
                    nombre, cantidad = linea.strip().split(',')
                    self.productos[nombre] = int(cantidad)
                print("Inventario cargado exitosamente.")
        except FileNotFoundError:    #Implementamos manejo de escepciones para posibles errores
            print("El archivo de inventario no existe. Se creará uno nuevo al añadir productos.")
        except PermissionError:      #Implementamos manejo de escepciones para posibles errores
            print("No se tienen los permisos necesarios para leer el archivo de inventario.")

    def guardar_inventario(self): #definimos una opción para guardar la nueva inofrmación en el archivo "Txt"
        try:
            with open("Deber Semana 9.txt", "w") as archivo:
                for nombre, cantidad in self.productos.items():
                    archivo.write(f"{nombre},{cantidad}\n")
                print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No se tienen los permisos necesarios para escribir en el archivo de inventario.")

    def anadir_producto(self, nombre, cantidad): # Definimos una función para añadir productos
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto '{nombre}' añadido/actualizado con éxito.")

    def actualizar_producto(self, nombre, cantidad):# Definimos una función para actualizar productos
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado con éxito.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):# Definimos una función para eliminar productos
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado con éxito.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")

# Ejemplo de uso
inventario = Inventario()
inventario.anadir_producto("Manzanas", 50)
inventario.actualizar_producto("Manzanas", 75)
inventario.eliminar_producto("Manzanas")

