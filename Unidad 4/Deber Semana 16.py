import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_completed(event=None):
    selected = tasks_list.curselection()
    if selected:
        task = tasks_list.get(selected)
        tasks_list.delete(selected)
        tasks_list.insert(tk.END, f"[Completada] {task}")
    else:
        messagebox.showinfo("Info", "Selecciona una tarea para marcarla como completada.")

def delete_task(event=None):
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected)
    else:
        messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

def close_app(event=None):
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")

# Campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Atajo para añadir con Enter

# Botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack()

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

# Lista de tareas
tasks_list = tk.Listbox(root, width=50, height=15)
tasks_list.pack(pady=10)

# Atajos de teclado adicionales
root.bind("<c>", mark_completed)  # Atajo para marcar como completada con "C"
root.bind("<d>", delete_task)    # Atajo para eliminar con "D"
root.bind("<Escape>", close_app) # Atajo para cerrar con "Escape"

# Iniciar el bucle de la aplicación
root.mainloop()
