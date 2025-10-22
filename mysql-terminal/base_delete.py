import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd2"
)
cursor = conexion.cursor()
sql = "DELETE FROM articulos WHERE id=%s;"
id_fila = [input("Ingrese el ID del articulo a eliminar: ")]
#id_fila = [id]

cursor.execute(sql, id_fila)
conexion.commit()
print("Registro eliminado, ID:", id_fila)
cursor.close()
conexion.close()