import mysql.connector

class Empleados:

    def abrir(self):
        conexion=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="",
                                            database="db2")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into empleado(nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas from empleado where empleado_id=%s"
        cursor.execute(sql, datos)
        resultados = cursor.fetchall()#Lo cambie de lugar ya que si no, no recupera datos
        cone.close()
        return resultados


    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas from empleado"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()


    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from empleado where empleado_id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update empleado set nombre=%s, apellido_paterno=%s, apellido_materno=%s, email=%s, fecha_contrato=%s, notas=%s where empleado_id=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas
