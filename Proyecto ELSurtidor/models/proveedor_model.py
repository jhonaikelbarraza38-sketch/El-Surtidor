from config.db import get_connection

def obtener_proveedores():
     conexion = get_connection()
     cursor = conexion.cursor()
     cursor.execute("SELECT id_proveedor, nombre, telefono, direccion, email FROM proveedor ORDER BY id_proveedor ASC ")
     datos = cursor.fetchall()
     cursor.close()
     conexion.close()
     return datos

def insertar_proveedor(nombre, telefono, direccion, email):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO proveedor (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, telefono, direccion, email))
    conexion.commit()
    conexion.close()

def actualizar_proveedor(id_proveedor, nombre, telefono, direccion, email):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE proveedor SET nombre = %s, telefono = %s, direccion = %s, email = %s WHERE id_proveedor = %s"
    cursor.execute(sql,(nombre, telefono, direccion, email, id_proveedor))
    conexion.commit()
    conexion.close()

def eliminar_proveedor(id_proveedor):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM proveedor WHERE id_proveedor = %s"
    cursor.execute(sql,(id_proveedor,))
    conexion.commit()
    conexion.close()