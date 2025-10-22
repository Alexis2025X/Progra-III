import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd2"
)
cursor = conexion.cursor()
sql =("INSERT into articulos(descripcion, precio) value (%s, %s);")
datos = ("Queso", 2.0)
cursor.execute(sql, datos)

conexion.commit()
#print("Registro insertado, ID:", cursor.lastrowid)
cursor.close()
conexion.close()