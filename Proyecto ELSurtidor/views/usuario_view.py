import tkinter as tk
from tkinter import ttk, messagebox
from controllers.usuario_controller import (
    guardar_usuario,
    listar_usuarios,
    editar_usuario,
    borrar_usuario
)
from models.usuario_model import validar_usuario

# iid almacena el id_usuario de forma oculta en el Treeview (no visible al usuario)
# values=fila[1:] muestra solo el username en la tabla

def ventana_usuarios(master):
    id_seleccionado = {"valor": None}
    username_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Usuarios")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- FORMULARIO --------
    frame_form = tk.Frame(ventana, padx=10, pady=10)
    frame_form.pack(fill="x")

    frame_form.columnconfigure(0, weight=1)
    frame_form.columnconfigure(1, weight=1)

    tk.Label(frame_form, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_username = tk.Entry(frame_form, width=25)
    entry_username.grid(row=1, column=0, padx=10, pady=5)

    tk.Label(frame_form, text="Password nueva:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
    entry_password = tk.Entry(frame_form, show="*", width=25)
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    # -------- TABLA --------
    frame_tabla = tk.Frame(ventana, padx=10, pady=10)
    frame_tabla.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame_tabla, columns=("Username",), show="headings")
    tree.heading("Username", text="Username")
    tree.column("Username", width=200, anchor="center")
    tree.pack(fill="both", expand=True)

    # -------- FUNCIONES --------
    def cargar_datos():
        for fila in tree.get_children():
            tree.delete(fila)
        datos = listar_usuarios()
        for fila in datos:
            tree.insert("", tk.END, iid=fila[0], values=fila[1:])

    def limpiar():
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        id_seleccionado["valor"] = None
        username_seleccionado["valor"] = None
        
    def nuevo():
        limpiar()

    def guardar():
        if guardar_usuario(entry_username.get(), entry_password.get()):
            limpiar()
            cargar_datos()

    def seleccionar(event):
        item = tree.selection()
        if item:
            id_seleccionado["valor"] = item[0]
            datos = tree.item(item)["values"]
            username_seleccionado["valor"] = datos[0]  # guarda el username para verificar después
            entry_username.delete(0, tk.END) # limpia el campo para evitar confusión, pero luego se muestra el username para facilitar la edición   
            entry_username.insert(0, datos[0])# username se muestra para facilitar la edición, pero password no se muestra por seguridad
            entry_password.delete(0, tk.END)  # password no se muestra por seguridad

    def editar():
        if not id_seleccionado["valor"]:    
            messagebox.showwarning("Advertencia", "Seleccione un usuario")
            return

        # Ventana para pedir contraseña actual
        ventana_verificar = tk.Toplevel(ventana)
        ventana_verificar.title("Verificar identidad")
        ventana_verificar.geometry("300x180")
        ventana_verificar.resizable(False, False)
        ventana_verificar.transient(ventana)
        ventana_verificar.grab_set()
        ventana_verificar.focus_force()

        tk.Label(ventana_verificar, text="Ingrese su contraseña actual:", font=("Arial", 11)).pack(pady=10)
        entry_pass_actual = tk.Entry(ventana_verificar, show="*", width=25)
        entry_pass_actual.pack(pady=5)
        entry_pass_actual.focus()

        def confirmar_edicion():
            pass_actual = entry_pass_actual.get().strip() 

            # Verifica que la contraseña actual sea correcta
            if not validar_usuario(username_seleccionado["valor"], pass_actual):
                messagebox.showerror("Error", "Contraseña actual incorrecta") # Si la contraseña es incorrecta, muestra un error y no permite continuar con la edición
                return

            nueva_password = entry_password.get().strip()  
            if not nueva_password:
                messagebox.showwarning("Advertencia", "Ingrese la nueva contraseña")
                return

            if editar_usuario(id_seleccionado["valor"], entry_username.get(), nueva_password):# Si la edición es exitosa, cierra la ventana de verificación, limpia el formulario y recarga los datos en la tabla
                ventana_verificar.destroy()
                limpiar()
                cargar_datos()

        tk.Button(ventana_verificar, text="Confirmar", width=15, command=confirmar_edicion).pack(pady=10)
        entry_pass_actual.bind("<Return>", lambda event: confirmar_edicion())

    def eliminar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un usuario")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este usuario?")
        if confirmar:
            if borrar_usuario(id_seleccionado["valor"]):
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