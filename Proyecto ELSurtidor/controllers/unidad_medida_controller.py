from models.unidad_medida_model import insertar_unidad, obtener_unidades, actualizar_unidad, eliminar_unidad
from tkinter import messagebox

def guardar_unidad(nombre):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False
    try:
        insertar_unidad(nombre)
        messagebox.showinfo("Éxito", "Unidad de medida registrada correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        return False

def listar_unidades():
    return obtener_unidades()

def editar_unidad(id_unidad, nombre):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False
    try:
        actualizar_unidad(id_unidad, nombre)
        messagebox.showinfo("Éxito", "Unidad de medida actualizada correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False

def borrar_unidad(id_unidad):
    try:
        eliminar_unidad(id_unidad)
        messagebox.showinfo("Éxito", "Unidad de medida eliminada correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se puede eliminar esta unidad porque tiene productos asociados")
        return False