import tkinter as tk
from tkinter import ttk, messagebox
from controllers.producto_controller import (
    guardar_producto,
    listar_productos,
    editar_producto,
    borrar_producto
)
from controllers.categoria_controller import listar_categorias
from controllers.proveedor_controller import listar_proveedores
from controllers.unidad_medida_controller import listar_unidades


def ventana_productos(master):
    id_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Productos")
    ventana.geometry("950x600")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- FORMULARIO --------
    frame_form = tk.Frame(ventana, padx=10, pady=10)
    frame_form.pack(fill="x")

    for i in range(4):
        frame_form.columnconfigure(i, weight=1) # Permite que las columnas se expandan proporcionalmente al tamaño del frame

    # Labels fila 0
    tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w")
    tk.Label(frame_form, text="Descripción:").grid(row=0, column=1, sticky="w")
    tk.Label(frame_form, text="Precio Compra:").grid(row=0, column=2, sticky="w")
    tk.Label(frame_form, text="Precio Venta:").grid(row=0, column=3, sticky="w")

    # Entries fila 1
    entry_nombre = tk.Entry(frame_form, width=25)
    entry_nombre.grid(row=1, column=0, sticky="w", padx=(0, 10))

    entry_descripcion = tk.Entry(frame_form, width=40)
    entry_descripcion.grid(row=1, column=1, sticky="w", padx=(0, 10))

    entry_precio_compra = tk.Entry(frame_form, width=18)
    entry_precio_compra.grid(row=1, column=2, sticky="w", padx=(0, 10))

    entry_precio_venta = tk.Entry(frame_form, width=18)
    entry_precio_venta.grid(row=1, column=3, sticky="w")

    # Labels fila 2
    tk.Label(frame_form, text="Stock:").grid(row=2, column=0, sticky="w")
    tk.Label(frame_form, text="Stock Mínimo:").grid(row=2, column=1, sticky="w")
    tk.Label(frame_form, text="Categoría:").grid(row=2, column=2, sticky="w")
    tk.Label(frame_form, text="Proveedor:").grid(row=2, column=3, sticky="w")

    # Entries fila 3
    entry_stock = tk.Entry(frame_form, width=18)
    entry_stock.grid(row=3, column=0, sticky="w", padx=(0, 10))

    entry_stock_minimo = tk.Entry(frame_form, width=18)
    entry_stock_minimo.grid(row=3, column=1, sticky="w", padx=(0, 10))

    combo_categoria = ttk.Combobox(frame_form, width=22, state="readonly")
    combo_categoria.grid(row=3, column=2, sticky="w", padx=(0, 10))

    combo_proveedor = ttk.Combobox(frame_form, width=22, state="readonly")
    combo_proveedor.grid(row=3, column=3, sticky="w")

    # Unidad de medida
    tk.Label(frame_form, text="Unidad de Medida:").grid(row=4, column=0, sticky="w")
    combo_unidad = ttk.Combobox(frame_form, width=22, state="readonly")
    combo_unidad.grid(row=5, column=0, sticky="w")

    # -------- COMBOBOX --------
    categorias, proveedores, unidades = [], [], [] # Listas para almacenar datos de categorías, proveedores y unidades

    def cargar_combobox():
        categorias.clear()
        categorias.extend(listar_categorias()) # extented agrega los elementos de la lista obtenida a la lista categorias sin reemplazarla, clear borra el contenido anterior para evitar duplicados
        combo_categoria["values"] = [c[1] for c in categorias] # muestra el nombre de la categoria como id es codigo interno [0] y nombre es [1] no se muestra, se recorren solo los nombres

        proveedores.clear()
        proveedores.extend(listar_proveedores())
        combo_proveedor["values"] = [p[1] for p in proveedores] # muestra el nombre del proveedor como id es codigo interno [0] y nombre es [1] no se muestra, se recorren solo los nombres

        unidades.clear()
        unidades.extend(listar_unidades())
        combo_unidad["values"] = [u[1] for u in unidades] # muestra el nombre de la unidad como id es codigo interno [0] y nombre es [1] no se muestra, se recorren solo los nombres

    # -------- TABLA --------
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(fill="both", expand=True)

    columnas = ("Nombre", "Descripción", "P.Compra", "P.Venta", "Stock", "Stock Min", "Categoría", "Proveedor", "Unidad")

    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings") # show = headings muestra todas las columnas sin la de identificacion (iid) que son los id_produtos y muestra el resto ya definidas

    tamaños = {
        "Nombre": 120,
        "Descripción": 300,
        "P.Compra": 80,
        "P.Venta": 80,
        "Stock": 60,
        "Stock Min": 80,
        "Categoría": 100,
        "Proveedor": 130,
        "Unidad": 80
    }

    for col in columnas: 
        tree.heading(col, text=col) # recorre cada columna y asigna el texto del encabezado
        tree.column(col, width=tamaños[col], anchor="center")# asigna el ancho y la alineación

    scroll_x = ttk.Scrollbar(frame_tabla, orient="horizontal", command=tree.xview)# permite desplazar horizontalmente la tabla cuando el contenido excede el ancho visible
    tree.configure(xscrollcommand=scroll_x.set)

    tree.pack(fill="both", expand=True)# ocupa todo el espacio disponible en el frame y se expande si la ventana cambia de tamaño
    scroll_x.pack(fill="x")

    # -------- FUNCIONES --------
    def cargar_datos():
        tree.delete(*tree.get_children())#limpia la tabla
        for fila in listar_productos(): # recorre e inserta y el id producto no se muestra 
            tree.insert("", tk.END, iid=fila[0], values=(
                fila[1], fila[2], fila[3], fila[4],
                fila[5], fila[6], fila[8], fila[10], fila[12] #7 9 y 11 son los id que no queremos mostrar de categoria, proveedor y unidad_medida
            ))

    def limpiar():
        for entry in [entry_nombre, entry_descripcion, entry_precio_compra,
                      entry_precio_venta, entry_stock, entry_stock_minimo]:# limpia cada entry del formulario
            entry.delete(0, tk.END) # borra el contenido desde la posición 0 hasta el final (END)
        combo_categoria.set("") # limpia el combo box seleccionando una opción vacía
        combo_proveedor.set("")
        combo_unidad.set("")
        id_seleccionado["valor"] = None # Reinicia el ID seleccionado a None para indicar que no hay ningún producto seleccionado actualmente
    
    def nuevo():
        limpiar()

    def guardar():
        if combo_categoria.current() < 0 or combo_proveedor.current() < 0 or combo_unidad.current() < 0: # Verifica si no se ha seleccionado una opción 
            messagebox.showwarning("Advertencia", "Seleccione categoría, proveedor y unidad")
            return
        if guardar_producto(
            entry_nombre.get(), entry_descripcion.get(),
            entry_precio_compra.get(), entry_precio_venta.get(),
            entry_stock.get(), entry_stock_minimo.get(),
            categorias[combo_categoria.current()][0],
            proveedores[combo_proveedor.current()][0],
            unidades[combo_unidad.current()][0]
        ):
            limpiar()
            cargar_datos()

    def seleccionar(event):
        item = tree.selection()
        if item:
            id_seleccionado["valor"] = item[0]
            datos = tree.item(item)["values"]

            # Limpiar antes de insertar para evitar acumulación de datos
            for entry in [entry_nombre, entry_descripcion, entry_precio_compra,
                          entry_precio_venta, entry_stock, entry_stock_minimo]:
                entry.delete(0, tk.END)

            entry_nombre.insert(0, datos[0])# datos[0] es el nombre porque el id no se muestra en la tabla
            entry_descripcion.insert(0, datos[1])
            entry_precio_compra.insert(0, datos[2])
            entry_precio_venta.insert(0, datos[3])
            entry_stock.insert(0, datos[4])
            entry_stock_minimo.insert(0, datos[5])

            combo_categoria.set(datos[6]) # datos[6] es el nombre de la categoría porque el id_categoria no se muestra en la tabla
            combo_proveedor.set(datos[7])
            combo_unidad.set(datos[8])

    def editar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de modificar este producto?")
        if  confirmar:
            if combo_categoria.current() < 0 or combo_proveedor.current() < 0 or combo_unidad.current() < 0:
                messagebox.showwarning("Advertencia", "Seleccione categoría, proveedor y unidad")
                return
        if editar_producto(
            id_seleccionado["valor"],
            entry_nombre.get(), entry_descripcion.get(),
            entry_precio_compra.get(), entry_precio_venta.get(),
            entry_stock.get(), entry_stock_minimo.get(),
            categorias[combo_categoria.current()][0],#[0] para obtener el id_categoria de la lista categorias así con todas 
            proveedores[combo_proveedor.current()][0],
            unidades[combo_unidad.current()][0]
        ):
            limpiar()
            cargar_datos()

    def eliminar():
        if not id_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
            if borrar_producto(id_seleccionado["valor"]):
                limpiar()
                cargar_datos()

    tree.bind("<<TreeviewSelect>>", seleccionar)

    # -------- BOTONES --------
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Nuevo", width=10, command=nuevo).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Guardar", width=10, command=guardar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Editar", width=10, command=editar).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Eliminar", width=10, command=eliminar).pack(side="left", padx=5)

    cargar_combobox()
    cargar_datos()