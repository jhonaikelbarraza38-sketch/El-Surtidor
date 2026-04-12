from models.producto_model import obtener_productos, insertar_producto, actualizar_producto, eliminar_producto, obtener_productos_stock_bajo, agregar_stock
from tkinter import messagebox

def guardar_producto(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False

    if float(precio_venta) <= float(precio_compra):
        messagebox.showwarning("Advertencia", "El precio de venta no puede ser menor o igual al precio de compra")
        return False
    # 1. Stock no puede ser negativo
    if int(stock) < 0:
        messagebox.showwarning("Advertencia", "El stock no puede ser negativo")
        return False

# 2. Stock mínimo no puede ser negativo
    if int(stock_minimo) < 0:
        messagebox.showwarning("Advertencia", "El stock mínimo no puede ser negativo")
        return False


# 3. Stock mínimo no puede ser mayor al stock actual
    if int(stock_minimo) > int(stock):
        messagebox.showwarning("Advertencia", "El stock mínimo no puede ser mayor al stock actual")
        return False
    
    try:
        insertar_producto(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida)
        messagebox.showinfo("Éxito", "Producto registrado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        return False
    

def listar_productos():
    return obtener_productos()

def editar_producto(id_producto, nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False

    if float(precio_venta) <= float(precio_compra):
        messagebox.showwarning("Advertencia", "El precio de venta no puede ser menor o igual al precio de compra")
        return False
    # 1. Stock no puede ser negativo
    if int(stock) < 0:
        messagebox.showwarning("Advertencia", "El stock no puede ser negativo")
        return False

    # 2. Stock mínimo no puede ser negativo
    if int(stock_minimo) < 0:
        messagebox.showwarning("Advertencia", "El stock mínimo no puede ser negativo")
        return False


    # 3. Stock mínimo no puede ser mayor al stock actual
    if int(stock_minimo) > int(stock):
        messagebox.showwarning("Advertencia", "El stock mínimo no puede ser mayor al stock actual")
        return False
    
    try: 
        actualizar_producto(id_producto, nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida)
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False
    
def borrar_producto(id_producto):
    try:
        eliminar_producto(id_producto)
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se puede eliminar este producto porque tiene pedidos asociados")
        return False
    
    #seccion de inventario 
def listar_stock_bajo():
    return obtener_productos_stock_bajo()

def actualizar_stock(id_producto, cantidad):
    try:
        agregar_stock(id_producto, cantidad)
        messagebox.showinfo("Éxito", "Stock actualizado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False
    