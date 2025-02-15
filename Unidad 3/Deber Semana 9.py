class Producto:
    def __init__(self, identidad, nombre, cantidad, precio):
        self.__identidad = identidad
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_identidad(self):
        return self.__identidad

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__identidad}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: ${self.__precio}"

class Inventario:
    def __init__(self):
        self.productos = []

    def anadir_producto(self, producto):
        for prod in self.productos:
            if prod.get_identidad() == producto.get_identidad():
                print("ID ya existente.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, identidad):
        for prod in self.productos:
            if prod.get_identidad() == identidad:
                self.productos.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, identidad, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_identidad() == identidad:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for prod in self.productos:
                print(prod)
        else:
            print("No hay productos en el inventario.")

def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            identidad = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            producto = Producto(identidad, nombre, cantidad, precio)
            inventario.anadir_producto(producto)
        elif opcion == '2':
            identidad = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(identidad)
        elif opcion == '3':
            identidad = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (dejar en blanco si no desea cambiar): ")
            precio = input("Ingresa el nuevo precio (dejar en blanco si no desea  cambiar): ")
            inventario.actualizar_producto(identidad, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == '4':
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
