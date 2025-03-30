import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task.strip() != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_task_completed():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        current_task = listbox_tasks.get(selected_task)
        listbox_tasks.delete(selected_task)
        listbox_tasks.insert(selected_task, f"[Tarea Completada] {current_task}")
    else:
        messagebox.showinfo("Información", "Por favor, selecciona una tarea para marcarla como completada.")

def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        listbox_tasks.delete(selected_task)
    else:
        messagebox.showinfo("Información", "Por favor, selecciona una tarea para eliminarla.")

def on_enter_pressed(event):
    add_task()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.grid(row=0, column=0, padx=10, pady=10)
entry_task.bind("<Return>", on_enter_pressed)

# Botones
btn_add_task = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add_task.grid(row=0, column=1, padx=10, pady=10)

btn_mark_completed = tk.Button(root, text="Marcar como Completada", command=mark_task_completed)
btn_mark_completed.grid(row=1, column=0, padx=10, pady=10)

btn_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete_task.grid(row=1, column=1, padx=10, pady=10)

# Lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
