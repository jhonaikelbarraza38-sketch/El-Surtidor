from models.reporte_model import ventas_por_cliente, ventas_por_producto
from models.producto_model import obtener_productos_stock_bajo
from tkinter import messagebox

def reporte_ventas_cliente(fecha_inicio, fecha_fin):
    if not fecha_inicio or not fecha_fin:
        messagebox.showwarning("Advertencia", "Ingrese el rango de fechas")
        return []
    try:
        return ventas_por_cliente(fecha_inicio, fecha_fin)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el reporte: {e}")
        return []

def reporte_ventas_producto(fecha_inicio, fecha_fin):
    if not fecha_inicio or not fecha_fin:
        messagebox.showwarning("Advertencia", "Ingrese el rango de fechas")
        return []
    try:
        return ventas_por_producto(fecha_inicio, fecha_fin)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el reporte: {e}")
        return []

def reporte_stock_bajo():
    try:
        return obtener_productos_stock_bajo()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el reporte: {e}")
        return []