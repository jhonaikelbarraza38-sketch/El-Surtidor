from config.db import get_connection

def validar_usuario(username, password):
    conexion = get_connection()
    if conexion is None:
        return None
    cursor = conexion.cursor()
    sql = "SELECT * FROM usuario WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conexion.close()
    return result

# -------- GESTIÓN DE USUARIOS --------

def obtener_usuarios():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_usuario, username FROM usuario ORDER BY id_usuario ASC")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos

def insertar_usuario(username, password):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    cursor.execute(sql, (username, password))
    conexion.commit()
    cursor.close()
    conexion.close()

def actualizar_usuario(id_usuario, username, password):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"
    cursor.execute(sql, (username, password, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_usuario(id_usuario):
    conexion = get_connection()
    cursor = conexion.cursor()
    sql = "DELETE FROM usuario WHERE id_usuario = %s"
    cursor.execute(sql, (id_usuario,))
    conexion.commit()
    cursor.close()
    conexion.close()