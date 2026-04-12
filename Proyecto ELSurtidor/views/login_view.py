import tkinter as tk
from controllers.usuario_controller import login, guardar_usuario
from tkinter import messagebox


def iniciar_login():

    ventana = tk.Tk()
    ventana.title("Login - El Surtidor")
    ventana.geometry("500x400")

    # Usuario
    tk.Label(ventana, text="Username", font=("Arial", 11)).pack(pady=5)
    entry_usuario = tk.Entry(ventana, width=25)
    entry_usuario.pack(pady=5)

    # Contraseña
    tk.Label(ventana, text="Password", font=("Arial", 11)).pack(pady=5)
    entry_password = tk.Entry(ventana, show="*", width=25)
    entry_password.pack(pady=5)

    def validar():
        user = entry_usuario.get().strip()
        password = entry_password.get().strip()

        if login(user, password):
            messagebox.showinfo("Éxito", "¡Bienvenido!")
            ventana.destroy()
            from views.menu_view import menu_principal
            menu_principal()
        else:
            messagebox.showerror("Error", "Datos incorrectos")

    def abrir_crear_usuario():
        ventana_crear = tk.Toplevel(ventana)
        ventana_crear.title("Crear Usuario")
        ventana_crear.geometry("300x250")
        ventana_crear.resizable(False, False)
        ventana_crear.transient(ventana)
        ventana_crear.grab_set()
        ventana_crear.focus_force()

        tk.Label(ventana_crear, text="Username:", font=("Arial", 11)).pack(pady=5)
        entry_new_user = tk.Entry(ventana_crear, width=25)
        entry_new_user.pack(pady=5)

        tk.Label(ventana_crear, text="Password:", font=("Arial", 11)).pack(pady=5)
        entry_new_pass = tk.Entry(ventana_crear, show="*", width=25)
        entry_new_pass.pack(pady=5)

        tk.Label(ventana_crear, text="Confirmar Password:", font=("Arial", 11)).pack(pady=5)
        entry_confirm_pass = tk.Entry(ventana_crear, show="*", width=25)
        entry_confirm_pass.pack(pady=5)

        def crear():
            username = entry_new_user.get().strip()
            password = entry_new_pass.get().strip()
            confirmar = entry_confirm_pass.get().strip()

            if not username or not password:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
                return
            if password != confirmar:
                messagebox.showerror("Error", "Las contraseñas no coinciden")
                return
            if guardar_usuario(username, password):
                ventana_crear.destroy()

        tk.Button(ventana_crear, text="Crear", width=15, command=crear).pack(pady=10)

    entry_usuario.bind("<Return>", lambda event: entry_password.focus())
    entry_password.bind("<Return>", lambda event: validar())
    entry_usuario.focus()

    tk.Button(ventana, text="Ingresar", width=15, command=validar).pack(pady=10)
    tk.Button(ventana, text="Crear Usuario", width=15, command=abrir_crear_usuario).pack(pady=5)

    ventana.mainloop()