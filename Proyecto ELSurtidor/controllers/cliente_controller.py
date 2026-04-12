from models.cliente_model import insertar_cliente, obtener_clientes, actualizar_cliente, eliminar_cliente
from tkinter import messagebox

def guardar_cliente(nombre, telefono, direccion, email):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False
    try:
        insertar_cliente(nombre, telefono, direccion, email)
        messagebox.showinfo("Éxito", "Cliente registrado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        return False

def listar_clientes():
    return obtener_clientes()

def editar_cliente(id_cliente, nombre, telefono, direccion, email):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False
    try:
        actualizar_cliente(id_cliente, nombre, telefono, direccion, email)
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False

def borrar_cliente(id_cliente):
    try:
        eliminar_cliente(id_cliente)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se puede eliminar este cliente porque tiene pedidos asociados")
        return False