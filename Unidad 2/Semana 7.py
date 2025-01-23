class Archivo: #Creamos la clase
    def __init__(self, nombre): #metodo constructor y parametros
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print("")
        print(f"Archivo {self.nombre} abierto.")

    def escribir(self, contenido): #Definimos atributos
        self.archivo.write(contenido)
        print(f"Escribiendo en {self.nombre}: {contenido}")

    def __del__(self):#metodo destructor
        self.archivo.close()
        print(f"Archivo {self.nombre} cerrado.") #establecemos mensaje de cierre de archivo


class ConexionBaseDatos:#Creamos otra clase para establecer la conexion a base de Datos
    def __init__(self, nombre):#metodo constructor
        self.nombre = nombre
        self.conectar()

    def conectar(self):#definimos la funcion "Conectar"
        print(f"Conectando a la base de datos {self.nombre}")
        self.conexion_establecida = True

    def desconectar(self): #definimos la funcion "Desconectar"
        print(f"Desconectando de la base de datos {self.nombre}")
        self.conexion_establecida = False

    def __del__(self):#definimos el metodo destructor para eliminar y cerrar
        self.desconectar()
        print(f"Conexión a la base de datos {self.nombre} cerrada.")


def main():
    # Crear y utilizar instancia de Archivo
    archivo = Archivo("Deber_Semana 7.txt")
    archivo.escribir('Bienvenidos a POO/ Metodo Constructor y Metodo Destructor')

    # Crear y utilizar instancia de Conexion Base de Datos
    ConexionBaseDatos('Mi Base de Datos')


if __name__ == "__main__": #Apliacmos el dunder name
    main()


