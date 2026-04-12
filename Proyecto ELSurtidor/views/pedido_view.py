import tkinter as tk
from tkinter import ttk, messagebox
from controllers.pedido_controller import (
    registrar_pedido,
    listar_pedidos,
    listar_pedidos_filtrados,
    listar_detalles,
    cambiar_estado,
    eliminar_pedido_completo
)
from controllers.cliente_controller import listar_clientes
from controllers.producto_controller import listar_productos

def ventana_pedidos(master):
    id_pedido_seleccionado = {"valor": None}
    detalles_temp = []

    ventana = tk.Toplevel(master)
    ventana.title("Gestión de Pedidos")
    ventana.geometry("1000x700")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- FRAME NUEVO PEDIDO --------
    frame_top = tk.Frame(ventana, padx=10, pady=10)
    frame_top.pack(fill="x")

    frame_top.columnconfigure(0, weight=1)
    frame_top.columnconfigure(1, weight=1)
    frame_top.columnconfigure(2, weight=1)
    frame_top.columnconfigure(3, weight=1)
    frame_top.columnconfigure(4, weight=1)

    tk.Label(frame_top, text="Cliente:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5)
    combo_cliente = ttk.Combobox(frame_top, width=25, state="readonly")
    combo_cliente.grid(row=1, column=0, padx=5, pady=3, sticky="w")

    tk.Label(frame_top, text="Producto:", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5)
    combo_producto = ttk.Combobox(frame_top, width=25, state="readonly")
    combo_producto.grid(row=1, column=1, padx=5, pady=3, sticky="w")

    tk.Label(frame_top, text="Cantidad:", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5)
    entry_cantidad = tk.Entry(frame_top, width=10)
    entry_cantidad.grid(row=1, column=2, padx=5, pady=3, sticky="w")

    tk.Button(frame_top, text="Agregar Producto", width=15,
              command=lambda: agregar_producto()).grid(row=1, column=3, padx=5, pady=3)

    tk.Button(frame_top, text="Confirmar Pedido", width=15, bg="green", fg="white",
              command=lambda: confirmar_pedido()).grid(row=1, column=4, padx=5, pady=3)

    # -------- TABLA DETALLE TEMPORAL --------
    tk.Label(frame_top, text="Productos en el pedido actual:", 
             font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=5, sticky="w", padx=5, pady=5)

    frame_detalle_temp = tk.Frame(frame_top)
    frame_detalle_temp.grid(row=3, column=0, columnspan=5, sticky="ew", padx=5)

    tree_detalle_temp = ttk.Treeview(frame_detalle_temp,
                                      columns=("Producto", "Cantidad", "Precio Unit", "Subtotal"),
                                      show="headings", height=5)
    tree_detalle_temp.heading("Producto", text="Producto")
    tree_detalle_temp.heading("Cantidad", text="Cantidad")
    tree_detalle_temp.heading("Precio Unit", text="Precio Unit")
    tree_detalle_temp.heading("Subtotal", text="Subtotal")

    tree_detalle_temp.column("Producto", width=200, anchor="center")
    tree_detalle_temp.column("Cantidad", width=80, anchor="center")
    tree_detalle_temp.column("Precio Unit", width=100, anchor="center")
    tree_detalle_temp.column("Subtotal", width=100, anchor="center")
    tree_detalle_temp.pack(fill="x")

    tk.Button(frame_top, text="Quitar seleccionado", width=15,
              command=lambda: quitar_producto()).grid(row=4, column=0, padx=5, pady=3, sticky="w")

    # -------- FILTROS --------
    frame_filtros = tk.Frame(ventana, padx=10, pady=5, relief="groove", bd=1)
    frame_filtros.pack(fill="x", padx=10)

    tk.Label(frame_filtros, text="Filtros:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
    tk.Label(frame_filtros, text="Cliente:").grid(row=0, column=1, padx=5, sticky="w")
    entry_filtro_cliente = tk.Entry(frame_filtros, width=20)
    entry_filtro_cliente.grid(row=0, column=2, padx=5)

    tk.Label(frame_filtros, text="Fecha (YYYY-MM-DD):").grid(row=0, column=3, padx=5, sticky="w")
    entry_filtro_fecha = tk.Entry(frame_filtros, width=15)
    entry_filtro_fecha.grid(row=0, column=4, padx=5)

    tk.Label(frame_filtros, text="Estado:").grid(row=0, column=5, padx=5, sticky="w")
    combo_filtro_estado = ttk.Combobox(frame_filtros, width=15, state="readonly",
                                        values=["", "pendiente", "despachado", "cancelado"])
    combo_filtro_estado.grid(row=0, column=6, padx=5)

    tk.Button(frame_filtros, text="Buscar", width=8,
              command=lambda: filtrar_pedidos()).grid(row=0, column=7, padx=5)
    tk.Button(frame_filtros, text="Limpiar", width=8,
              command=lambda: limpiar_filtros()).grid(row=0, column=8, padx=5)

    # -------- TABLA PEDIDOS --------
    frame_pedidos = tk.Frame(ventana, padx=10, pady=5)
    frame_pedidos.pack(fill="both", expand=True)

    tk.Label(frame_pedidos, text="Pedidos registrados:", font=("Arial", 10, "bold")).pack(anchor="w")

    tree_pedidos = ttk.Treeview(frame_pedidos,
                                 columns=("Cliente", "Fecha", "Estado", "Total"),
                                 show="headings", height=8)
    tree_pedidos.heading("Cliente", text="Cliente")
    tree_pedidos.heading("Fecha", text="Fecha")
    tree_pedidos.heading("Estado", text="Estado")
    tree_pedidos.heading("Total", text="Total")

    tree_pedidos.column("Cliente", width=180, anchor="center")
    tree_pedidos.column("Fecha", width=150, anchor="center")
    tree_pedidos.column("Estado", width=100, anchor="center")
    tree_pedidos.column("Total", width=100, anchor="center")
    tree_pedidos.pack(fill="both", expand=True)

    # -------- TABLA DETALLE PEDIDO SELECCIONADO --------
    frame_detalle = tk.Frame(ventana, padx=10, pady=5)
    frame_detalle.pack(fill="x")

    tk.Label(frame_detalle, text="Detalle del pedido seleccionado:", 
             font=("Arial", 10, "bold")).pack(anchor="w")

    tree_detalle = ttk.Treeview(frame_detalle,
                                 columns=("Producto", "Cantidad", "Precio Unit", "Subtotal"),
                                 show="headings", height=4)
    tree_detalle.heading("Producto", text="Producto")
    tree_detalle.heading("Cantidad", text="Cantidad")
    tree_detalle.heading("Precio Unit", text="Precio Unit")
    tree_detalle.heading("Subtotal", text="Subtotal")

    tree_detalle.column("Producto", width=200, anchor="center")
    tree_detalle.column("Cantidad", width=80, anchor="center")
    tree_detalle.column("Precio Unit", width=100, anchor="center")
    tree_detalle.column("Subtotal", width=100, anchor="center")
    tree_detalle.pack(fill="x")

    # -------- COMBOBOX DATA --------
    clientes = []
    productos = []

    def cargar_combobox():
        clientes.clear()
        clientes.extend(listar_clientes())
        combo_cliente["values"] = [c[1] for c in clientes]

        productos.clear()
        productos.extend(listar_productos())
        combo_producto["values"] = [p[1] for p in productos]

    # -------- FUNCIONES --------
    def cargar_pedidos():
        tree_pedidos.delete(*tree_pedidos.get_children())
        for fila in listar_pedidos():
            tree_pedidos.insert("", tk.END, iid=fila[0], values=(
                fila[1], fila[2], fila[3], ""
            ))

    def agregar_producto():
        idx_prod = combo_producto.current()
        if idx_prod < 0:
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

        producto = productos[idx_prod]
        id_producto = producto[0]
        nombre = producto[1]
        precio_unitario = producto[4]
        subtotal = cantidad * precio_unitario

        for d in detalles_temp:
            if d[0] == id_producto:
                messagebox.showwarning("Advertencia", "El producto ya está en el pedido")
                return

        detalles_temp.append((id_producto, nombre, cantidad, precio_unitario))
        tree_detalle_temp.insert("", tk.END, values=(nombre, cantidad, precio_unitario, subtotal))
        entry_cantidad.delete(0, tk.END)

    def quitar_producto():
        item = tree_detalle_temp.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Seleccione un producto para quitar")
            return
        idx = tree_detalle_temp.index(item)
        detalles_temp.pop(idx)
        tree_detalle_temp.delete(item)

    def confirmar_pedido():
        idx_cli = combo_cliente.current()
        if idx_cli < 0:
            messagebox.showwarning("Advertencia", "Seleccione un cliente")
            return
        if not detalles_temp:
            messagebox.showwarning("Advertencia", "Agregue al menos un producto al pedido")
            return

        id_cliente = clientes[idx_cli][0]

        if registrar_pedido(id_cliente, detalles_temp):
            detalles_temp.clear()
            tree_detalle_temp.delete(*tree_detalle_temp.get_children())
            combo_cliente.set("")
            combo_producto.set("")
            id_pedido_seleccionado["valor"] = None          # limpia selección
            tree_detalle.delete(*tree_detalle.get_children())  # limpia detalle
            cargar_pedidos()
            cargar_combobox()

    def seleccionar_pedido(event):
        item = tree_pedidos.selection()
        if item:
            id_pedido_seleccionado["valor"] = item[0]
            tree_detalle.delete(*tree_detalle.get_children())
            for fila in listar_detalles(item[0]):
                tree_detalle.insert("", tk.END, values=fila[1:])

    def filtrar_pedidos():
        cliente = entry_filtro_cliente.get().strip() or None
        fecha = entry_filtro_fecha.get().strip() or None
        estado = combo_filtro_estado.get() or None

        tree_pedidos.delete(*tree_pedidos.get_children())
        for fila in listar_pedidos_filtrados(cliente, fecha, estado):
            tree_pedidos.insert("", tk.END, iid=fila[0], values=(
                fila[1], fila[2], fila[3], ""
            ))

    def limpiar_filtros():
        entry_filtro_cliente.delete(0, tk.END)
        entry_filtro_fecha.delete(0, tk.END)
        combo_filtro_estado.set("")
        cargar_pedidos()

    def cambiar_a_despachado():
        if not id_pedido_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un pedido")
            return
        if cambiar_estado(id_pedido_seleccionado["valor"], None, "despachado"):
            cargar_pedidos()

    def cambiar_a_cancelado():
        if not id_pedido_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un pedido")
            return
        confirmar = messagebox.askyesno("Confirmar", 
                    "¿Cancelar este pedido? El inventario no se restaurará.")
        if confirmar:
            if cambiar_estado(id_pedido_seleccionado["valor"], None, "cancelado"):
                cargar_pedidos()

    def eliminar_pedido():
        if not id_pedido_seleccionado["valor"]:
            messagebox.showwarning("Advertencia", "Seleccione un pedido")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar este pedido?"):
            if eliminar_pedido_completo(id_pedido_seleccionado["valor"]):
                id_pedido_seleccionado["valor"] = None
                tree_detalle.delete(*tree_detalle.get_children())
                cargar_pedidos()

    # -------- EVENTO --------
    tree_pedidos.bind("<<TreeviewSelect>>", seleccionar_pedido)

    # -------- BOTONES --------
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Marcar Despachado", width=16,
              command=cambiar_a_despachado).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Cancelar Pedido", width=16, fg="red",
              command=cambiar_a_cancelado).pack(side="left", padx=5)
    tk.Button(frame_botones, text="Eliminar Pedido", width=16,
              command=eliminar_pedido).pack(side="left", padx=5)

    # -------- CARGA INICIAL --------
    cargar_combobox()
    cargar_pedidos()