import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd2"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM articulos;")
for datos in cursor:
    print(datos)
conexion.close()
