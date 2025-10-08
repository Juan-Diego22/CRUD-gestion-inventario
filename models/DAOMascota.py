from config.conexion import Conexion
from entities.cMascota import Mascota
from mysql.connector import *

class DAOMascota(Conexion):
    def listarMascotas(self):
        #con un condicional vamos a verificar conexion
        if self.conexion.is_connected():
        
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM mascotas")
                resultados = cursor.fetchall() 
                return resultados
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        else:
            print("Error: No hay conexión")

        cursor.close()


    def registrarMascota(self, m = Mascota()):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO mascotas(nombre, especie, raza, edad, propietario) VALUES (%s, %s, %s, %s, %s)"
                datos = (m.getNombre(), m.getEspecie(), m.getRaza(), m.getEdad(), m.getPropietario())
                cursor.execute(sql, datos)
                self.conexion.commit()
                print("Mascota registrada con exito \n")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
        else:
            print("Error no hay conexion")  
        cursor.close()

    def editarMascota(self, m = Mascota()):
    
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """
                UPDATE mascotas
                SET nombre = %s,
                    especie = %s,
                    raza = %s,
                    edad = %s,
                    propietario = %s
                WHERE id_mascota = %s
                """
                datos = (m.getNombre(),m.getEspecie(),m.getRaza (),m.getEdad(),m.getPropietario(),m.getId_Mascota())
                cursor.execute(sql, datos)
                self.conexion.commit()
                print("Mascota editada con exito \n")
            except Error as ex:
                print(f"Error al intentar actualizar {ex}")
        else:
            print("Error no hay conexion")         
        cursor.close()

    def eliminarMascota(self, id_mascota):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM mascotas WHERE id_mascota = %s"
                datos = (id_mascota,)  # la coma hace que sea una tupla
                cursor.execute(sql, datos)
                self.conexion.commit()
                print(f"Mascota con ID {id_mascota} eliminada con éxito.\n")
            except Error as ex:
                print(f" Error al intentar eliminar: {ex}")
        else:
            print(" Error: no hay conexión")
        