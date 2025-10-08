from config.conexion import Conexion
from entities.cConsulta import Consulta
from mysql.connector import *

class DAOConsulta(Conexion):
     #metodo para ver los productos
    def listarConsultas(self):
        
        if self.conexion.is_connected():
            
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM consultas")
                resultados = cursor.fetchall() 
                cursor.close()
                return resultados
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        else:
            print("Error: No hay conexión")

    def registrarConsultas(self, c = Consulta()):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """
                    INSERT INTO consultas (mascota_id, fechaHora, motivo, tratamiento, medico, costo)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                datos = (
                    c.getMascota_id(),
                    c.getFechaHora(),
                    c.getMotivo(),
                    c.getTratamiento(),
                    c.getMedico(),
                    c.getCosto()
                    )
                cursor.execute(sql, datos)
                self.conexion.commit()
                print("Consulta registrada con éxito.\n")
            except Exception as ex:
                print(f"Ha ocurrido un error al registrar la consulta: {ex}")
        else:
            print("Error: No hay conexión a la base de datos.")
            

    def editarConsulta(self, c = Consulta()):
    
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """
                UPDATE consultas
                SET mascota_id = %s,
                    fechaHora = %s,
                    motivo = %s,
                    tratamiento = %s,
                    medico = %s,
                    costo = %s
                WHERE id_consulta = %s
                """
                datos = (c.getMascota_id(),c.getFechaHora(),c.getMotivo() \
                        ,c.getTratamiento(),c.getMedico(),c.getCosto(),c.getId_Consulta())
                cursor.execute(sql, datos)
                self.conexion.commit()
                print("Consulta editada con exito \n")
            except Error as ex:
                print(f"Error al intentar actualizar {ex}")
        else:
            print("Error no hay conexion") 


    def eliminarConsulta(self, id_consulta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM consultas WHERE id_consulta = %s"
                datos = (id_consulta,)
                cursor.execute(sql, datos)
                self.conexion.commit()
                print(f"Consulta con ID {id_consulta} eliminada con éxito.\n")
            except Error as ex:
                print(f"Error al intentar eliminar: {ex}")
        else:
            print("Error: no hay conexión")
                       