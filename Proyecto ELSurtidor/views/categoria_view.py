import tkinter as tk
from tkinter import ttk, messagebox
from controllers.categoria_controller import (
    guardar_categoria,
    listar_categorias,
    editar_categoria,
    borrar_categoria
)

# iid almacena el id_categoria de forma oculta en el Treeview (no visible al usuario)
# values=fila[1:] muestra solo el nombre en la tabla

def ventana_categorias(master):
    id_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Categorías")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- FORMULARIO --------
    frame_form = tk.Frame(ventana, padx=10, pady=10)
    frame_form.pack(fill="x")

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    # -------- TABLA --------
    frame_tabla = tk.Frame(ventana, padx=10, pady=10)
    frame_tabla.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame_tabla, columns=("Nombre",), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.column("Nombre", width=200, anchor="center")
    tree.pack(fill="both", expand=True)

    # -------- FUNCIONES --------
    def cargar_datos():
        for fila in tree.get_children():
            tree.delete(fila)
        datos = listar_categorias()
        for fila in datos:
            tree.insert("", tk.END, iid=fila[0], values=fila[1:])

    def limpiar():
        entry_nombre.delete(0, tk.END)
        id_seleccionado["valor"] = None  # ✅ también limpia el id seleccionado

    def nuevo():
        limpiar()  # ✅ limpia el formulario para ingresar una nueva categoría

    def guardar():
        if guardar_categoria(entry_nombre.get()):
            limpiar()
            cargar_datos()

    def seleccionar(event):
        item = tree.selection()
        if item:
            id_seleccionado["valor"] = item[0]
            datos = tree.item(item)["values"]
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, datos[0])

    def editar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione una categoría")
            return
        
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de modificar esta categoría?")
        if confirmar:
            if editar_categoria(id_seleccionado["valor"], entry_nombre.get()):
                limpiar()
                cargar_datos()

    def eliminar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione una categoría")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta categoría?")
        if confirmar:
            if borrar_categoria(id_seleccionado["valor"]):
                limpiar()
                cargar_datos()

    # -------- EVENTO --------
    tree.bind("<<TreeviewSelect>>", seleccionar)

    # -------- BOTONES --------
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Nuevo", width=10, command=nuevo).pack(side="left", padx=5)      
    tk.Button(frame_botones, text="Guardar", width=10, command=guardar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Editar", width=10, command=editar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar).pack(side="left", padx=5)

    # -------- CARGA INICIAL --------
    cargar_datos()