import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana de información")
ventana.geometry("300x400")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Lista para mostrar datos
tabla = ttk.Treeview(ventana, columns="Datos", show="headings")
tabla.heading("Datos", text="Información")
tabla.pack(pady=10)

# Función para agregar datos
def agregar_datos():
    texto = entrada.get()
    if texto:  # Verifica que no esté vacío
        tabla.insert("", "end", values=(texto,))
        entrada.delete(0, tk.END)  # Limpia el campo de texto

# Función para limpiar datos seleccionados o todos
def limpiar_datos():
    for item in tabla.get_children():
        tabla.delete(item)  # Elimina todas las filas

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_datos)
boton_agregar.pack(pady=5)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal
ventana.mainloop()



