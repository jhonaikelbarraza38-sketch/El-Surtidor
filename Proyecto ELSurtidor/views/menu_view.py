import tkinter as tk
from views.categoria_view import ventana_categorias
from views.proveedor_view import ventana_proveedores
from views.cliente_view import ventana_clientes
from views.unidad_medida_view import ventana_unidades
from views.usuario_view import ventana_usuarios
from views.producto_view import ventana_productos
from views.pedido_view import ventana_pedidos
from views.inventario_view import ventana_inventario
from views.reporte_view import ventana_reportes

def menu_principal():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("400x300")
    ventana.resizable(False, False)

    ventana.focus_force()

    barra_superior = tk.Menu(ventana) # barra de menú

    menu_productos = tk.Menu(barra_superior, tearoff=0) 
    menu_categorias = tk.Menu(barra_superior, tearoff=0)
    menu_proveedores = tk.Menu(barra_superior, tearoff=0)
    menu_clientes = tk.Menu(barra_superior, tearoff=0)
    menu_pedidos = tk.Menu(barra_superior, tearoff=0)
    menu_usuarios = tk.Menu(barra_superior, tearoff=0)
    menu_inventario = tk.Menu(barra_superior, tearoff=0)
    menu_reportes = tk.Menu(barra_superior, tearoff=0)  

    menu_productos.add_command(label="Gestionar Productos", command=lambda: ventana_productos(ventana))
    menu_productos.add_command(label="Gestionar Unidades de Medida", command=lambda: ventana_unidades(ventana))
    menu_categorias.add_command(label="Gestionar Categorías",command=lambda: ventana_categorias(ventana))
    menu_proveedores.add_command(label="Gestionar Proveedores", command=lambda: ventana_proveedores(ventana))
    menu_clientes.add_command(label="Gestionar Clientes", command=lambda: ventana_clientes(ventana))
    menu_usuarios.add_command(label="Gestionar Usuarios", command=lambda: ventana_usuarios(ventana))
    menu_pedidos.add_command(label="Gestionar Pedidos", command=lambda: ventana_pedidos(ventana))
    menu_inventario.add_command(label="Gestión de Inventario", command=lambda: ventana_inventario(ventana))
    menu_reportes.add_command(label="Generar Reportes", command=lambda: ventana_reportes(ventana))

    ventana.config(menu=barra_superior)# Agrega la barra de menú a la ventana principal

    barra_superior.add_cascade(label="Productos", menu=menu_productos)
    barra_superior.add_cascade(label="Categorías", menu=menu_categorias)
    barra_superior.add_cascade(label="Proveedores", menu=menu_proveedores)
    barra_superior.add_cascade(label="Clientes", menu=menu_clientes)
    barra_superior.add_cascade(label="Pedidos", menu=menu_pedidos)
    barra_superior.add_cascade(label="Usuarios", menu=menu_usuarios)
    barra_superior.add_cascade(label="Inventario", menu=menu_inventario)
    barra_superior.add_cascade(label="Reportes", menu=menu_reportes)
    
    titulo = tk.Label(
        ventana,
        text="Sistema de Gestión - El Surtidor",
        font=("Arial", 16, "bold")
    )
    titulo.pack(pady=110)

    ventana.mainloop()

    

 