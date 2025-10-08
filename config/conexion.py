import mysql.connector
from mysql.connector import *

class Conexion(object):
    conexion ="" #cadena de conexion
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost", #127.0.0.1
                port = 3306,
                user = "root",
                password = "1040326889",
                db = "gestion_consultas_veterinarias"
            )   
        except Error as ex:   
            print(f"Error en la conexion: {ex}")
        else:
            print("Conexión exitosa")

#Conexion = Conexion()                