from config.db import get_connection

def insertar_detalle(id_pedido, id_producto, cantidad, precio_unitario, subtotal):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = """INSERT INTO detalle_pedido 
             (id_pedido, id_producto, cantidad, precio_unitario, subtotal) 
             VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql, (id_pedido, id_producto, cantidad, precio_unitario, subtotal))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_detalles_por_pedido(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT dp.id_detalle_pedido, p.nombre, dp.cantidad, 
               dp.precio_unitario, dp.subtotal
        FROM detalle_pedido dp
        JOIN producto p ON dp.id_producto = p.id_producto
        WHERE dp.id_pedido = %s # filtra por el id_pedido para obtener solo los detalles de ese pedido específico (un solo pedido a la vez)
    """, (id_pedido,))
    datos = cursor.fetchall() # trae los detalles del pedido específico (un solo pedido a la vez) para mostrar en la página de detalles del pedido.
    cursor.close()
    conexion.close()
    return datos # retorna los detalles del pedido específico (un solo pedido a la vez) para mostrar en la página de detalles del pedido.

    #no hay actualizar detalle_pedido (se debe eliminar el detalle_pedid y hacer uno nuevo)

def eliminar_detalles_por_pedido(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM detalle_pedido WHERE id_pedido = %s"
    cursor.execute(sql, (id_pedido,)) # elimina todos los detalles asociados a un pedido específico
    conexion.commit()
    cursor.close()
    conexion.close()