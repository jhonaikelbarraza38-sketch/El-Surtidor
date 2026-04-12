from models.categoria_model import insertar_categoria, obtener_categorias, actualizar_categoria, eliminar_categoria
from tkinter import messagebox


def guardar_categoria(nombre):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False

    try:
        insertar_categoria(nombre)
        messagebox.showinfo("Éxito", "Categoría registrada correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
        return False


def listar_categorias():
    return obtener_categorias()

def editar_categoria(id_categoria, nombre):
    if not nombre.strip():
        messagebox.showwarning("Advertencia", "El nombre es obligatorio")
        return False

    try:
        actualizar_categoria(id_categoria, nombre)
        messagebox.showinfo("Éxito", "Categoría actualizada")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False
    

def borrar_categoria(id_categoria):
    try:
        eliminar_categoria(id_categoria)
        messagebox.showinfo("Éxito", "Categoría eliminada correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se puede eliminar esta categoría porque tiene productos asociados")
        return False