from models.proveedor_model import insertar_proveedor, obtener_proveedores, actualizar_proveedor, eliminar_proveedor
from tkinter import messagebox

def guardar_proveedor(nombre, telefono, direccion, email):
    if not nombre.strip():
        messagebox.showwarning("advertencia", "El nombre es obligatorio")
        return False
    
    try: 
        insertar_proveedor(nombre, telefono, direccion, email)
        messagebox.showinfo("Éxito", "Proveedor registrado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        return False    
    
def listar_proveedores():
    return obtener_proveedores()

def editar_proveedor(id_proveedor, nombre, telefono, direccion, email):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False

    try:
        actualizar_proveedor(id_proveedor, nombre, telefono, direccion, email)
        messagebox.showinfo("Éxito", "Proveedor actualizado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False
    
def borrar_proveedor(id_proveedor):
    try:
        eliminar_proveedor(id_proveedor)
        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se puede eliminar este proveedor porque tiene productos asociados")
        return False