from config.db import get_connection

def obtener_clientes():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_cliente, nombre, telefono, direccion, email FROM cliente ORDER BY id_cliente ASC")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def insertar_cliente(nombre, telefono, direccion, email):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO cliente (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, direccion, email))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_cliente(id_cliente, nombre, telefono, direccion, email):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE cliente SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id_cliente = %s"
    cursor.execute(sql, (nombre, telefono, direccion, email, id_cliente))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_cliente(id_cliente):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM cliente WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    conexion.commit()
    cursor.close()
    conexion.close()