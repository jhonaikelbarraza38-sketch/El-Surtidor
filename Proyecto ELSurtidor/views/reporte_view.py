import tkinter as tk
from tkinter import ttk, messagebox
from controllers.reporte_controller import (
    reporte_ventas_cliente,
    reporte_ventas_producto,
    reporte_stock_bajo
)

def ventana_reportes(master):
    ventana = tk.Toplevel(master)
    ventana.title("Módulo de Reportes")
    ventana.geometry("900x600")
    ventana.resizable(False, False)

    ventana.transient(master)
    ventana.grab_set()
    ventana.focus_force()

    # -------- NOTEBOOK --------
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # -------- PESTAÑA 1 - VENTAS POR CLIENTE --------
    frame_cliente = tk.Frame(notebook, padx=10, pady=10)
    notebook.add(frame_cliente, text="Ventas por Cliente")

    frame_filtro1 = tk.Frame(frame_cliente)
    frame_filtro1.pack(fill="x", pady=5)

    tk.Label(frame_filtro1, text="Fecha inicio (YYYY-MM-DD):").grid(row=0, column=0, padx=5, sticky="w")
    entry_inicio1 = tk.Entry(frame_filtro1, width=15)
    entry_inicio1.grid(row=0, column=1, padx=5)

    tk.Label(frame_filtro1, text="Fecha fin (YYYY-MM-DD):").grid(row=0, column=2, padx=5, sticky="w")
    entry_fin1 = tk.Entry(frame_filtro1, width=15)
    entry_fin1.grid(row=0, column=3, padx=5)

    tk.Button(frame_filtro1, text="Generar", width=10,
              command=lambda: generar_reporte_cliente()).grid(row=0, column=4, padx=5)

    tk.Button(frame_filtro1, text="Limpiar", width=10,
              command=lambda: limpiar_cliente()).grid(row=0, column=5, padx=5)

    tree_cliente = ttk.Treeview(frame_cliente,
                                 columns=("Cliente", "Total Pedidos", "Total Ventas"),
                                 show="headings")
    tree_cliente.heading("Cliente", text="Cliente")
    tree_cliente.heading("Total Pedidos", text="Total Pedidos")
    tree_cliente.heading("Total Ventas", text="Total Ventas ($)")

    tree_cliente.column("Cliente", width=200, anchor="center")
    tree_cliente.column("Total Pedidos", width=120, anchor="center")
    tree_cliente.column("Total Ventas", width=150, anchor="center")
    tree_cliente.pack(fill="both", expand=True, pady=10)

    label_total1 = tk.Label(frame_cliente, text="", font=("Arial", 10, "bold"))
    label_total1.pack(anchor="e", padx=10)

    # -------- PESTAÑA 2 - VENTAS POR PRODUCTO --------
    frame_producto = tk.Frame(notebook, padx=10, pady=10)
    notebook.add(frame_producto, text="Ventas por Producto")

    frame_filtro2 = tk.Frame(frame_producto)
    frame_filtro2.pack(fill="x", pady=5)

    tk.Label(frame_filtro2, text="Fecha inicio (YYYY-MM-DD):").grid(row=0, column=0, padx=5, sticky="w")
    entry_inicio2 = tk.Entry(frame_filtro2, width=15)
    entry_inicio2.grid(row=0, column=1, padx=5)

    tk.Label(frame_filtro2, text="Fecha fin (YYYY-MM-DD):").grid(row=0, column=2, padx=5, sticky="w")
    entry_fin2 = tk.Entry(frame_filtro2, width=15)
    entry_fin2.grid(row=0, column=3, padx=5)

    tk.Button(frame_filtro2, text="Generar", width=10,
              command=lambda: generar_reporte_producto()).grid(row=0, column=4, padx=5)

    tk.Button(frame_filtro2, text="Limpiar", width=10,
              command=lambda: limpiar_producto()).grid(row=0, column=5, padx=5)

    tree_producto = ttk.Treeview(frame_producto,
                                  columns=("Producto", "Cantidad Vendida", "Total Ventas"),
                                  show="headings")
    tree_producto.heading("Producto", text="Producto")
    tree_producto.heading("Cantidad Vendida", text="Cantidad Vendida")
    tree_producto.heading("Total Ventas", text="Total Ventas ($)")

    tree_producto.column("Producto", width=200, anchor="center")
    tree_producto.column("Cantidad Vendida", width=130, anchor="center")
    tree_producto.column("Total Ventas", width=150, anchor="center")
    tree_producto.pack(fill="both", expand=True, pady=10)

    label_total2 = tk.Label(frame_producto, text="", font=("Arial", 10, "bold"))
    label_total2.pack(anchor="e", padx=10)

    # -------- PESTAÑA 3 - STOCK BAJO MÍNIMO --------
    frame_stock = tk.Frame(notebook, padx=10, pady=10)
    notebook.add(frame_stock, text="Stock Bajo Mínimo")

    tk.Button(frame_stock, text="Actualizar", width=10,
              command=lambda: cargar_stock_bajo()).pack(anchor="w", pady=5)

    tree_stock = ttk.Treeview(frame_stock,
                               columns=("Nombre", "Categoría", "Stock", "Stock Mín"),
                               show="headings")
    tree_stock.heading("Nombre", text="Nombre")
    tree_stock.heading("Categoría", text="Categoría")
    tree_stock.heading("Stock", text="Stock Actual")
    tree_stock.heading("Stock Mín", text="Stock Mínimo")

    tree_stock.column("Nombre", width=180, anchor="center")
    tree_stock.column("Categoría", width=120, anchor="center")
    tree_stock.column("Stock", width=100, anchor="center")
    tree_stock.column("Stock Mín", width=100, anchor="center")
    tree_stock.pack(fill="both", expand=True)

    tree_stock.tag_configure("bajo", background="red", foreground="white")

    # -------- FUNCIONES --------
    def generar_reporte_cliente():
        datos = reporte_ventas_cliente(entry_inicio1.get().strip(), entry_fin1.get().strip())
        tree_cliente.delete(*tree_cliente.get_children())
        total = 0
        for fila in datos:
            tree_cliente.insert("", tk.END, values=fila)
            total += fila[2]
        label_total1.config(text=f"Total ventas: ${total:,.2f}")

    def limpiar_cliente():
        entry_inicio1.delete(0, tk.END)
        entry_fin1.delete(0, tk.END)
        tree_cliente.delete(*tree_cliente.get_children())
        label_total1.config(text="")

    def generar_reporte_producto():
        datos = reporte_ventas_producto(entry_inicio2.get().strip(), entry_fin2.get().strip())
        tree_producto.delete(*tree_producto.get_children())
        total = 0
        for fila in datos:
            tree_producto.insert("", tk.END, values=fila)
            total += fila[2]
        label_total2.config(text=f"Total ventas: ${total:,.2f}")

    def limpiar_producto():
        entry_inicio2.delete(0, tk.END)
        entry_fin2.delete(0, tk.END)
        tree_producto.delete(*tree_producto.get_children())
        label_total2.config(text="")

    def cargar_stock_bajo():
        tree_stock.delete(*tree_stock.get_children())
        for fila in reporte_stock_bajo():
            # fila = (id_producto, nombre, stock, stock_minimo, nombre_categoria)
            tree_stock.insert("", tk.END, values=(
                fila[1], fila[4], fila[2], fila[3]
            ), tags=("bajo",))

    # -------- CARGA INICIAL --------
    cargar_stock_bajo()