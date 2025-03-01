#Importamos el formato Json
import json

#Creamos la clase Prodcuto
class Producto:
    def __init__(self, identidad, nombre, cantidad, precio):
        self.identidad = identidad
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.identidad}, Nombre: {self.nombre}, Cantidad {self.cantidad}, Precio ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario(self, archivo = "inventario.json"):
        try:
            with open(archivo, 'r') as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado, se procede a crear uno nuevo")
            self.productos = {}
        except json.JSONDecodeError:
            print("Error al intentar leer el archivo de inventario, Verifique que el formato sea el correcto")
            self.productos = {}

    def guardar_inventario(self, archivo = "inventario.json"):
        try:
            with open(archivo, "w") as f:
                json.dump(self.productos, f, indent=4)
        except Exception as e:
            print(f"Error al intentar guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.identidad in self.productos:
            print("Producto ya existente")
        else:
            self.productos[producto.identidad_producto] = producto.__dict__

    def eliminar_producto(self, identidad):
        if identidad in self.productos:
            del self.productos[identidad]
            print(f"Producto {identidad} actualizado")
        else:
            print("El producto que intenta eliminar no puedo ser encontrado")

    def actualizar_producto(self, identidad, cantidad = None, precio = None):
        if identidad in self.productos:
            if cantidad is not None:
                self.productos[identidad]["cantidad"] =   cantidad
            if precio is not None:
                self.productos[identidad]["precio"] = precio
            print(f"El producto {identidad} actualizado")
        else:
            print("Producto no existe")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío")
        else:
            for identidad, informacion in self.productos.items():
                try:
                    producto = Producto(identidad, informacion["nombre"], informacion["cantidad"], informacion["precio"])
                    print(producto)
                except KeyError as e:
                    print(f"Error al mostrar producto {identidad} ya que falta el campo {e}")

def menu():
    invetario = Inventario()
    invetario.cargar_inventario()

    while True:
        print("1.Agregar producto")
        print("2.Eliminar producto")
        print("3.Actualizar producto")
        print("4.Mostrar Inventario")

        opcion = input("\nSeleccione una opción: ")
        while not opcion.isdigit():
            print("Lo sentimos en este apartado solo se puede ingresar números")
            opcion = input("\nSeleccione una opción: ")
        while opcion < "1" or opcion > "5":
            print("Lo sentimos, esa opción no existe")
            print("1.Agregar producto")
            print("2.Eliminar producto")
            print("3.Actualizar producto")
            print("4.Mostrar Inventario")
            opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            identidad = input("ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(identidad, nombre, cantidad, precio)
            invetario.agregar_producto(producto)
            invetario.guardar_inventario()
        elif opcion == "2":
            identidad = input("ID del producto: ")
            invetario.eliminar_producto(identidad)
            invetario.guardar_inventario()
        elif opcion == "3":
            identidad = input("ID del producto que desea actualizar: ")
            cantidad = int(input("Ingrese la cantidad que desa actualizar: "))
            precio = float(input("Ingrese el nuevo precio: "))
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            invetario.actualizar_producto(identidad, cantidad, precio)
            invetario.guardar_inventario()
        elif opcion == "4":
            invetario.mostrar_inventario()
        else:
            invetario.guardar_inventario()
            break

if __name__ == "__main__":
    menu()










