# import mysql.connector
#
# class Articulos:
#     def abrir(self):
#         conexion = mysql.connector.connect(
#                             host="localhost",
#                             user="root",
#                             password="",
#                             database="ugb01")
#         return conexion
#     def guardar(self, datos):
#         cone = self.abrir()
#         cursor = cone.cursor()
#         sql = "INSERT into productos(nombre, precio) value (%s, %s);"
#         cursor.execute(sql, datos)
#         cone.commit()
#         cone.close()
#
#     def consulta(self, datos):
#         cone = self.abrir()
#         cursor = cone.cursor()
#         sql = "SELECT descripcion, precio FROM productos WHERE codigo=%s;"
#         cursor.execute(sql, datos)
#         cone.close()
#         return cursor.fetchall()
#
#     def recuperar_todos(self):
#         cone = self.abrir()
#         cursor = cone.cursor()
#         sql = "SELECT nombre, precio FROM productos;"
#         cursor.execute(sql)
#         cone.close()
#         return cursor.fetchall()
#
#     def baja(self, datos):
#         cone = self.abrir()
#         cursor = cone.cursor()
#         sql = "DELETE FROM productos WHERE id=%s;"
#         cursor.execute(sql, datos)
#         cone.close()
#         return cursor.rowcount() #Retorna la cantidad de filas afectadas
#
#     def modificar(self, datos):
#         cone = self.abrir()
#         cursor = cone.cursor()
#         sql = "UPDATE producto SET nombre=%s, precio=%s WHERE id=%s;"
#         cursor.execute(sql, datos)
#         cone.commit()
#         cone.close()
#         return cursor.rowcount()