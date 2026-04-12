from models.usuario_model import validar_usuario
from models.usuario_model import validar_usuario, obtener_usuarios, insertar_usuario, actualizar_usuario, eliminar_usuario
from tkinter import messagebox

def login(username, password):
    if not username or not password:
        return False
    
    resultado = validar_usuario(username, password)

    if resultado is None:
        return False
    else:
        return True
    

def guardar_usuario(username, password):
    if not username.strip() or not password.strip():
        messagebox.showwarning("Advertencia", "Username y password son obligatorios")
        return False
    try:
        insertar_usuario(username, password)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", "No se pudo guardar, el username ya existe")
        return False

def listar_usuarios():
    return obtener_usuarios()

def editar_usuario(id_usuario, username, password):
    if not username.strip() or not password.strip():
        messagebox.showwarning("Advertencia", "Username y password son obligatorios")
        return False
    try:
        actualizar_usuario(id_usuario, username, password)
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar: {e}")
        return False

def borrar_usuario(id_usuario):
    try:
        eliminar_usuario(id_usuario)
        messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar: {e}")
        return False