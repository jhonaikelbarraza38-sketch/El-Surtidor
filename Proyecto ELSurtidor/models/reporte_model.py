from config.db import get_connection

def ventas_por_cliente(fecha_inicio, fecha_fin):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT c.nombre AS cliente,
               COUNT(p.id_pedido) AS total_pedidos,
               SUM(dp.subtotal) AS total_ventas
        FROM pedido p
        JOIN cliente c ON p.id_cliente = c.id_cliente
        JOIN detalle_pedido dp ON p.id_pedido = dp.id_pedido
        WHERE DATE(p.fecha) BETWEEN %s AND %s
        AND p.estado != 'cancelado'
        GROUP BY c.id_cliente, c.nombre
        ORDER BY total_ventas DESC
    """, (fecha_inicio, fecha_fin))
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def ventas_por_producto(fecha_inicio, fecha_fin):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT pr.nombre AS producto,
               SUM(dp.cantidad) AS total_vendido,
               SUM(dp.subtotal) AS total_ventas
        FROM detalle_pedido dp
        JOIN producto pr ON dp.id_producto = pr.id_producto
        JOIN pedido p ON dp.id_pedido = p.id_pedido
        WHERE DATE(p.fecha) BETWEEN %s AND %s
        AND p.estado != 'cancelado'
        GROUP BY pr.id_producto, pr.nombre
        ORDER BY total_ventas DESC
    """, (fecha_inicio, fecha_fin))
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos