from models.pedido_model import insertar_pedido, obtener_pedidos, actualizar_estado_pedido, eliminar_pedido, obtener_pedidos_filtrados
from models.detalle_pedido_model import insertar_detalle, obtener_detalles_por_pedido, eliminar_detalles_por_pedido
from models.producto_model import verificar_stock, descontar_stock
from tkinter import messagebox

def registrar_pedido(id_cliente, detalles):
    # detalles = [(id_producto, nombre, cantidad, precio_unitario), ...]

    # Validar stock de todos los productos antes de registrar
    for detalle in detalles:
        id_producto, nombre, cantidad, precio_unitario = detalle
        if not verificar_stock(id_producto, cantidad):
            messagebox.showwarning("Stock insuficiente", f"No hay suficiente stock para: {nombre}")
            return False

    try:
        # Insertar el pedido y obtener su id
        id_pedido = insertar_pedido(id_cliente)

        # Insertar cada detalle y descontar stock
        for detalle in detalles:
            id_producto, nombre, cantidad, precio_unitario = detalle
            subtotal = cantidad * precio_unitario
            insertar_detalle(id_pedido, id_producto, cantidad, precio_unitario, subtotal)
            descontar_stock(id_producto, cantidad)

        messagebox.showinfo("Éxito", "Pedido registrado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo registrar el pedido: {e}")
        return False

def listar_pedidos():
    return obtener_pedidos()

def listar_pedidos_filtrados(cliente=None, fecha=None, estado=None):
    return obtener_pedidos_filtrados(cliente, fecha, estado)

def listar_detalles(id_pedido):
    return obtener_detalles_por_pedido(id_pedido)

def cambiar_estado(id_pedido, estado_actual, nuevo_estado):
    # Al cancelar un pedido despachado no se restaura el inventario
    try:
        actualizar_estado_pedido(id_pedido, nuevo_estado)
        messagebox.showinfo("Éxito", f"Estado actualizado a: {nuevo_estado}")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el estado: {e}")
        return False

def eliminar_pedido_completo(id_pedido):
    try:
        eliminar_detalles_por_pedido(id_pedido)
        eliminar_pedido(id_pedido)
        messagebox.showinfo("Éxito", "Pedido eliminado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el pedido: {e}")
        return False