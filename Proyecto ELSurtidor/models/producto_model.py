from config.db import get_connection

def obtener_productos():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT 
            p.id_producto,
            p.nombre,
            p.descripcion,
            p.precio_compra,
            p.precio_venta,
            p.stock,
            p.stock_minimo,
            p.id_categoria,
            c.nombre AS categoria,
            p.id_proveedor,
            pr.nombre AS proveedor,
            p.id_unidad_medida,
            u.nombre AS unidad_medida
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        JOIN proveedor pr ON p.id_proveedor = pr.id_proveedor
        JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
        ORDER BY p.id_producto ASC
    """)
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def insertar_producto(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO producto (nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql,(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida))
    conexion.commit()
    conexion.close()

def actualizar_producto(id_producto, nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE producto SET nombre = %s, descripcion = %s, precio_compra = %s, precio_venta = %s, stock = %s, stock_minimo = %s, id_categoria = %s, id_proveedor = %s, id_unidad_medida = %s WHERE id_producto = %s"
    cursor.execute(sql,(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida, id_producto))
    conexion.commit()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM producto WHERE id_producto = %s"
    cursor.execute(sql, (id_producto,))
    conexion.commit()
    conexion.close()

#estas dos es para la seccion de pedidos

def verificar_stock(id_producto, cantidad):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT stock FROM producto WHERE id_producto = %s", (id_producto,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado[0] >= cantidad  # trae el valor de la columna stock (resultado[0]) y lo compara con la cantidad solicitada para verificar si hay suficiente stock disponible para esa cantidad.
    #debe retornar True si hay suficiente stock (resultado[0] >= cantidad) o False si no hay suficiente stock (resultado[0] < cantidad) para que el controlador pueda decidir si permite agregar el producto al pedido o muestra un mensaje de error por falta de stock.


def descontar_stock(id_producto, cantidad):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE producto SET stock = stock - %s WHERE id_producto = %s" # actualiza el stock del producto restando la cantidad vendida (stock = stock - cantidad) para reflejar la venta en la base de datos.
    cursor.execute(sql, (cantidad, id_producto))
    conexion.commit()
    cursor.close()
    conexion.close()

# estas dos para inventario
def obtener_productos_stock_bajo():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.id_producto, p.nombre, p.stock, p.stock_minimo,
               c.nombre AS categoria
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE p.stock <= p.stock_minimo
        ORDER BY p.stock ASC
    """)
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def agregar_stock(id_producto, cantidad):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE producto SET stock = stock + %s WHERE id_producto = %s"
    cursor.execute(sql, (cantidad, id_producto))
    conexion.commit()
    cursor.close()
    conexion.close()

