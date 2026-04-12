from config.db import get_connection

def obtener_categorias():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_categoria, nombre FROM categoria ORDER BY id_categoria ASC")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos


def insertar_categoria(nombre):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO categoria (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    conexion.close()

def actualizar_categoria(id_categoria, nombre):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE categoria SET nombre = %s WHERE id_categoria = %s"
    cursor.execute(sql, (nombre, id_categoria))
    conexion.commit()
    conexion.close()


def eliminar_categoria(id_categoria):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM categoria WHERE id_categoria = %s"
    cursor.execute(sql, (id_categoria,))
    conexion.commit()
    conexion.close()