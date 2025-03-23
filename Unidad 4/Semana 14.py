# Importamos la librería Tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

#Creamos Una clase que contenga los atributos
class AgendaApp:
    def __init__(self, rot):
        self.rot = rot
        self.rot.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = tk.Frame(rot)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para campos de entrada
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        # Creamos los labels de la fecha (lo que mostraremos al usuario a traves del apliactivo gráfico)
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.calendar = Calendar(self.frame_entrada, date_pattern="yyyy-mm-dd")
        self.calendar.grid(row=0, column=1, padx=5, pady=5)

        # Creamos los labels de la hora (lo que mostraremos al usuario a traves del apliactivo gráfico)
        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        # Creamos los labels de la descripcion (lo que mostraremos al usuario a traves del apliactivo gráfico)
        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_desc = tk.Entry(self.frame_entrada, width=30)
        self.entry_desc.grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=5)
        tk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    #Definimos la funcion para agregar un nuevo evento
    def agregar_evento(self):
        fecha = self.calendar.get_date()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()
        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        else: #Nos aseguramos de que en caso de no estar llenos los campos, salte una alerta
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")

    # Definimos la funcion para eliminar un evento
    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            self.tree.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


# Ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()



