import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd2"
)
cursor = conexion.cursor()

sql = "UPDATE articulos SET descripcion=%s, precio=%s WHERE id=%s;"
id_fila = input("Ingrese el ID del articulo a modificar: ")
#id_fila = [id]
descripcion = input("Ingrese la nueva descripcion: ")
precio = input("Ingrese el nuevo precio: ")
datos = (descripcion, precio, id_fila)

cursor.execute(sql, datos)
conexion.commit()
print("Registro modificado, ID:", id_fila)
cursor.close()
conexion.close()