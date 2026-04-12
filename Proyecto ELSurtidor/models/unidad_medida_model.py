from config.db import get_connection

def obtener_unidades():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_unidad_medida, nombre FROM unidad_medida ORDER BY id_unidad_medida ASC")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def insertar_unidad(nombre):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO unidad_medida (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_unidad(id_unidad, nombre):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE unidad_medida SET nombre = %s WHERE id_unidad_medida = %s"
    cursor.execute(sql, (nombre, id_unidad))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_unidad(id_unidad):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM unidad_medida WHERE id_unidad_medida = %s"
    cursor.execute(sql, (id_unidad,))
    conexion.commit()
    cursor.close()
    conexion.close()