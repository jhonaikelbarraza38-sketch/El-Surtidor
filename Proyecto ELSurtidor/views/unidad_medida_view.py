import tkinter as tk
from tkinter import ttk, messagebox
from controllers.unidad_medida_controller import (
    guardar_unidad,
    listar_unidades,
    editar_unidad,
    borrar_unidad
)

# iid almacena el id_unidad_medida de forma oculta en el Treeview (no visible al usuario)
# values=fila[1:] muestra solo el nombre en la tabla

def ventana_unidades(master):
    id_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Unidades de Medida")
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
        datos = listar_unidades()
        for fila in datos:
            tree.insert("", tk.END, iid=fila[0], values=fila[1:])

    def limpiar():
        entry_nombre.delete(0, tk.END)
        id_seleccionado["valor"] = None
    
    def nuevo():
        limpiar()

    def guardar():
        if guardar_unidad(entry_nombre.get()):
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
            messagebox.showwarning("Advertencia", "Seleccione una unidad de medida")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de modificar esta unidad de medida?")
        if confirmar:
            if editar_unidad(id_seleccionado["valor"], entry_nombre.get()):
                id_seleccionado["valor"] = None
                limpiar()
                cargar_datos()

    def eliminar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione una unidad de medida")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta unidad de medida?")
        if confirmar:
            if borrar_unidad(id_seleccionado["valor"]):
                id_seleccionado["valor"] = None
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