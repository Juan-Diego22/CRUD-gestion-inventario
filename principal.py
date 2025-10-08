from models.DAOConsulta import DAOConsulta
from models.DAOMascota import DAOMascota
from controllers.funciones import *

def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("\n====== MENÚ PRINCIPAL ======")
            print("1. Listar Mascotas")
            print("2. Registrar Mascota")
            print("3. Actualizar Mascota")
            print("4. Eliminar Mascota")
            print("5. Listar Consultas")
            print("6. Registrar Consulta")
            print("7. Actualizar Consulta")
            print("8. Eliminar Consulta")
            print("9. Salir")

            try:
                opcion = int(input("Seleccione una opción (1-9): "))
                if opcion < 1 or opcion > 9:
                    print("Opción inválida. Intente nuevamente.")
                else:
                    opcionCorrecta = True
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
       
        if opcion == 9:
            print("Saliendo...")
            input("Presione Enter para finalizar")
            continuar = False
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion in [1, 2, 3, 4]:
        ejecutarMascota(opcion)
    elif opcion in [5, 6, 7, 8]:
        ejecutarConsulta(opcion - 4)


# CRUD Mascotas
def ejecutarMascota(opcion):
    dao = DAOMascota()

    if opcion == 1:
        try:
            mascotas = dao.listarMascotas()
            if mascotas:
                listarMascotas(mascotas)
            else:
                print("No se encontraron mascotas.")
        except Exception as e:
            print(f"Error al listar mascotas: {e}")
    elif opcion == 2:
        mascota = getDatosRegistroMascota()
        try:
            dao.registrarMascota(mascota)
            print("Mascota registrada con éxito.")
        except Exception as e:
            print(f"Error al registrar mascota: {e}")
    elif opcion == 3:
        try:
            mascotas = dao.listarMascotas()
            mascota = getDatosEditarMascota(mascotas)
            if mascota:
                dao.editarMascota(mascota)
                print("Mascota actualizada con éxito.")
        except Exception as e:
            print(f"Error al actualizar mascota: {e}")
    elif opcion == 4:
        try:
            mascotas = dao.listarMascotas()
            id_mascota = getIdEliminarMascota(mascotas)
            dao.eliminarMascota(id_mascota)
            print("Mascota eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar mascota: {e}")


# CRUD Consultas
def ejecutarConsulta(opcion):
    dao = DAOConsulta()

    if opcion == 1:
        try:
            consultas = dao.listarConsultas()
            if consultas:
                listarConsultas(consultas)
            else:
                print("No se encontraron consultas.")
        except Exception as e:
            print(f"Error al listar consultas: {e}")
    elif opcion == 2:
        try:
            consultas = dao.listarConsultas()
            if consultas: 
                listarConsultas(consultas)

            consulta = getDatosRegistrarConsulta()
            dao.registrarConsultas(consulta)
            print("Consulta registrada con éxito.")
        except Exception as e:
            print(f"Error al registrar consulta: {e}")
    elif opcion == 3:
        try:
            consultas = dao.listarConsultas()
            consulta = getDatosEditarConsulta(consultas)
            if consulta:
                dao.editarConsulta(consulta)
                print("Consulta actualizada con éxito.")
        except Exception as e:
            print(f"Error al actualizar consulta: {e}")
    elif opcion == 4:
        try:
            consultas = dao.listarConsultas()
            id_consulta = getIdEliminarConsulta(consultas)
            dao.eliminarConsulta(id_consulta)
            print("Consulta eliminada con éxito.")
        except Exception as e:
            print(f"Error al eliminar consulta: {e}")


#  Ejecutar menú
menuPrincipal()            
              
                

        