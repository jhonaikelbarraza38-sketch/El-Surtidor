import tkinter as tk
from tkinter import ttk, messagebox
from controllers.cliente_controller import (
    guardar_cliente,
    listar_clientes,
    editar_cliente,
    borrar_cliente
)

# iid almacena el id_cliente de forma oculta en el Treeview (no visible al usuario)
# values=fila[1:] muestra solo nombre, teléfono, dirección, email en la tabla

def ventana_clientes(master):
    id_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Clientes")
    ventana.geometry("700x500")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- FORMULARIO --------
    frame_form = tk.Frame(ventana, padx=10, pady=10)
    frame_form.pack(fill="x")

    frame_form.columnconfigure(0, weight=1)
    frame_form.columnconfigure(1, weight=1)

    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nombre = tk.Entry(frame_form, width=25)
    entry_nombre.grid(row=1, column=0, padx=10, pady=5)

    tk.Label(frame_form, text="Teléfono:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_telefono = tk.Entry(frame_form, width=25)
    entry_telefono.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_form, text="Dirección:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_direccion = tk.Entry(frame_form, width=25)
    entry_direccion.grid(row=3, column=0, padx=10, pady=5)

    tk.Label(frame_form, text="Email:").grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entry_email = tk.Entry(frame_form, width=25)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    # -------- TABLA --------
    frame_tabla = tk.Frame(ventana, padx=10, pady=10)
    frame_tabla.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame_tabla, columns=("Nombre", "Teléfono", "Dirección", "Email"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Teléfono", text="Teléfono")
    tree.heading("Dirección", text="Dirección")
    tree.heading("Email", text="Email")

    tree.column("Nombre", width=150, anchor="center")
    tree.column("Teléfono", width=150, anchor="center")
    tree.column("Dirección", width=150, anchor="center")
    tree.column("Email", width=150, anchor="center")
    tree.pack(fill="both", expand=True)

    # -------- FUNCIONES --------
    def cargar_datos():
        for fila in tree.get_children():
            tree.delete(fila)
        datos = listar_clientes()
        for fila in datos:
            tree.insert("", tk.END, iid=fila[0], values=fila[1:])

    def limpiar():
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        id_seleccionado["valor"] = None

    def nuevo():
        limpiar()

    def guardar():
        if guardar_cliente(entry_nombre.get(), entry_telefono.get(), entry_direccion.get(), entry_email.get()):
            limpiar()
            cargar_datos()

    def seleccionar(event):
        item = tree.selection()
        if item:
            id_seleccionado["valor"] = item[0]
            datos = tree.item(item)["values"]

            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, datos[0])
            entry_telefono.delete(0, tk.END)
            entry_telefono.insert(0, datos[1])
            entry_direccion.delete(0, tk.END)
            entry_direccion.insert(0, datos[2])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, datos[3])

    def editar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de modificar este cliente?")
        if confirmar:
            if editar_cliente(id_seleccionado["valor"], entry_nombre.get(), entry_telefono.get(), entry_direccion.get(), entry_email.get()):
                id_seleccionado["valor"] = None
                limpiar()
                cargar_datos()

    def eliminar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este cliente?")
        if confirmar:
            if borrar_cliente(id_seleccionado["valor"]):
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