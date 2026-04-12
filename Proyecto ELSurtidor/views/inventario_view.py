import tkinter as tk
from tkinter import ttk, messagebox
from controllers.producto_controller import listar_productos, listar_stock_bajo, actualizar_stock

# iid almacena el id_producto de forma oculta en el Treeview

def ventana_inventario(master):
    id_seleccionado = {"valor": None}

    ventana = tk.Toplevel(master)
    ventana.title("Módulo de Inventario")
    ventana.geometry("900x600")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- NOTEBOOK (pestañas) --------
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # -------- PESTAÑA 1 - STOCK ACTUAL --------
    frame_stock = tk.Frame(notebook, padx=10, pady=10)
    notebook.add(frame_stock, text="Stock Actual")

    tk.Label(frame_stock, text="Stock actual de todos los productos:",
             font=("Arial", 10, "bold")).pack(anchor="w", pady=5)

    tree_stock = ttk.Treeview(frame_stock,
                               columns=("Nombre", "Categoría", "Stock", "Stock Mín", "Estado"),
                               show="headings")
    tree_stock.heading("Nombre", text="Nombre")
    tree_stock.heading("Categoría", text="Categoría")
    tree_stock.heading("Stock", text="Stock")
    tree_stock.heading("Stock Mín", text="Stock Mín")
    tree_stock.heading("Estado", text="Estado")

    tree_stock.column("Nombre", width=180, anchor="center")
    tree_stock.column("Categoría", width=120, anchor="center")
    tree_stock.column("Stock", width=80, anchor="center")
    tree_stock.column("Stock Mín", width=80, anchor="center")
    tree_stock.column("Estado", width=120, anchor="center")
    tree_stock.pack(fill="both", expand=True)

    # Tag para resaltar productos con stock bajo
    tree_stock.tag_configure("bajo", background="red", foreground="white")

    # -------- PESTAÑA 2 - ENTRADA DE MERCANCÍA --------
    frame_entrada = tk.Frame(notebook, padx=10, pady=10)
    notebook.add(frame_entrada, text="Entrada de Mercancía")

    tk.Label(frame_entrada, text="Seleccione un producto y agregue la cantidad recibida:",
             font=("Arial", 10, "bold")).pack(anchor="w", pady=5)

    frame_form = tk.Frame(frame_entrada)
    frame_form.pack(fill="x", pady=5)

    tk.Label(frame_form, text="Producto:").grid(row=0, column=0, padx=5, sticky="w")
    combo_producto = ttk.Combobox(frame_form, width=30, state="readonly")
    combo_producto.grid(row=0, column=1, padx=5)

    tk.Label(frame_form, text="Cantidad a agregar:").grid(row=0, column=2, padx=5, sticky="w")
    entry_cantidad = tk.Entry(frame_form, width=10)
    entry_cantidad.grid(row=0, column=3, padx=5)

    tk.Button(frame_form, text="Agregar Stock", width=15,
              command=lambda: agregar_stock_producto()).grid(row=0, column=4, padx=5)

    tk.Label(frame_entrada, text="Productos con stock bajo mínimo:",
             font=("Arial", 10, "bold")).pack(anchor="w", pady=5)

    tree_bajo = ttk.Treeview(frame_entrada,
                              columns=("Nombre", "Categoría", "Stock", "Stock Mín"),
                              show="headings")
    tree_bajo.heading("Nombre", text="Nombre")
    tree_bajo.heading("Categoría", text="Categoría")
    tree_bajo.heading("Stock", text="Stock Actual")
    tree_bajo.heading("Stock Mín", text="Stock Mínimo")

    tree_bajo.column("Nombre", width=180, anchor="center")
    tree_bajo.column("Categoría", width=120, anchor="center")
    tree_bajo.column("Stock", width=100, anchor="center")
    tree_bajo.column("Stock Mín", width=100, anchor="center")
    tree_bajo.pack(fill="both", expand=True)

    tree_bajo.tag_configure("bajo", background="red", foreground="white")

    # -------- FUNCIONES --------
    productos = []

    def cargar_stock_actual():
        tree_stock.delete(*tree_stock.get_children())
        for fila in listar_productos():
            # fila = (id, nombre, desc, precio_compra, precio_venta, stock, stock_minimo,
            #          id_cat, nombre_cat, id_prov, nombre_prov, id_uni, nombre_uni)
            stock_actual = fila[5]
            stock_minimo = fila[6]
            nombre_cat = fila[8]
            estado = "⚠ Bajo mínimo" if stock_actual <= stock_minimo else "✓ Normal"
            tag = "bajo" if stock_actual <= stock_minimo else ""
            tree_stock.insert("", tk.END, iid=fila[0], values=(
                fila[1], nombre_cat, stock_actual, stock_minimo, estado
            ), tags=(tag,))

    def cargar_stock_bajo():
        tree_bajo.delete(*tree_bajo.get_children())
        for fila in listar_stock_bajo():
            # fila = (id_producto, nombre, stock, stock_minimo, nombre_categoria)
            tree_bajo.insert("", tk.END, values=(
                fila[1], fila[4], fila[2], fila[3]
            ), tags=("bajo",))

    def cargar_combobox():
        productos.clear()
        productos.extend(listar_productos())
        combo_producto["values"] = [p[1] for p in productos]

    def agregar_stock_producto():
        idx = combo_producto.current()
        if idx < 0:
            messagebox.showwarning("Advertencia", "Seleccione un producto")
            return
        try:
            cantidad = int(entry_cantidad.get())
            if cantidad <= 0:
                messagebox.showwarning("Advertencia", "La cantidad debe ser mayor a 0")
                return
        except ValueError:
            messagebox.showwarning("Advertencia", "Ingrese una cantidad válida")
            return

        id_producto = productos[idx][0]
        if actualizar_stock(id_producto, cantidad):
            entry_cantidad.delete(0, tk.END)
            combo_producto.set("")
            cargar_stock_actual()
            cargar_stock_bajo()
            cargar_combobox()

    # -------- CARGA INICIAL --------
    cargar_stock_actual()
    cargar_stock_bajo()
    cargar_combobox()