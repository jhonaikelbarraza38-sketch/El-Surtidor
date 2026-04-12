from config.db import get_connection

def obtener_pedidos():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.id_pedido, c.nombre, p.fecha, p.estado
        FROM pedido p
        JOIN cliente c ON p.id_cliente = c.id_cliente
        ORDER BY p.id_pedido DESC
    """)
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def insertar_pedido(id_cliente):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO pedido (id_cliente) VALUES (%s)"
    cursor.execute(sql, (id_cliente,)) # los demas camopos se llenan con valores por defecto (fecha actual y estado 'pendiente')
    conexion.commit()
    id_nuevo = cursor.lastrowid  # retorna el id del pedido recién creado ((cursor.lastrowid)Cuando insertas un pedido la BD le asigna un id_pedido automático. lastrowid te dice cuál ID le asignó:)
    cursor.close()
    conexion.close()
    return id_nuevo # retorna el id del pedido recién creado para que el controlador pueda usarlo para redirigir a la página de detalles del pedido o para agregar productos al pedido recién creado.

def actualizar_estado_pedido(id_pedido, estado):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE pedido SET estado = %s WHERE id_pedido = %s"
    cursor.execute(sql, (estado, id_pedido))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_pedido(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM pedido WHERE id_pedido = %s"
    cursor.execute(sql, (id_pedido,))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_pedidos_filtrados(cliente=None, fecha=None, estado=None):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = """
        SELECT p.id_pedido, c.nombre, p.fecha, p.estado
        FROM pedido p
        JOIN cliente c ON p.id_cliente = c.id_cliente
        WHERE 1=1 
    """
    valores = []
    if cliente:
        sql += " AND c.nombre LIKE %s"
        valores.append(f"%{cliente}%")
    if fecha:
        sql += " AND DATE(p.fecha) = %s"
        valores.append(fecha)
    if estado:
        sql += " AND p.estado = %s"
        valores.append(estado)
    sql += " ORDER BY p.id_pedido DESC"
    cursor.execute(sql, valores)
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos