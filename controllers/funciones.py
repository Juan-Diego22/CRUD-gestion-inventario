from datetime import datetime
from entities.cConsulta import Consulta
from entities.cMascota import Mascota

# ---------- MASCOTAS ---------
def listarMascotas(mascotas):
    print("\n--- Lista de Mascotas ---")
    print("-" * 73)
    print(f"{'ID':<5} {'Nombre':<15} {'Especie':<15} {'Raza':<15} {'Edad':<5} {'Propietario':<15}")
    print("-" * 73)
    for m in mascotas:
        print(f"{m[0]:<5} {m[1]:<15} {m[2]:<15} {m[3]:<15} {m[4]:<5} {m[5]:<15}")
    print("-" * 73)

def getDatosRegistroMascota():
    nombre = input("Nombre: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    edad = int(input("Edad: "))
    propietario = input("Nombre del propietario: ").strip()

    mascota = Mascota()
    mascota.setNombre(nombre)
    mascota.setEspecie(especie)
    mascota.setRaza(raza)
    mascota.setEdad(edad)
    mascota.setPropietario(propietario)

    return mascota

def getDatosEditarMascota(lista):
    if not lista:
        print("No hay mascotas para editar.")
        return None

    print("\n--- Editar Mascota ---")
    for m in lista:
        print(f"{m[0]}. {m[1]} ({m[2]}) - Edad: {m[4]}")

    try:
        id_mascota = int(input("Ingrese el ID de la mascota a editar: "))
        nombre = input("Nuevo nombre: ").strip()
        especie = input("Nueva especie: ").strip()
        raza = input("Nueva raza: ").strip()
        edad = int(input("Nueva edad: "))
        propietario = input("Nuevo nombre del propietario: ").strip()

        mascota = Mascota()
        mascota.setId_Mascota(id_mascota)
        mascota.setNombre(nombre)
        mascota.setEspecie(especie)
        mascota.setRaza(raza)
        mascota.setEdad(edad)
        mascota.setPropietario(propietario)

        return mascota

    except ValueError:
        print("Entrada inválida. Verifica los datos.")
        return None

def getIdEliminarMascota(lista):
    listarMascotas(lista)
    id = input("ID de la mascota a eliminar: ").strip()
    if not id.isnumeric():
        print("ID inválido.")
        return None
    confirmar = input(f"¿Seguro que deseas eliminar la mascota con ID {id}? (s/n): ").lower()
    return int(id) if confirmar == "s" else None

# ---------- CONSULTAS ----------
def listarConsultas(consultas):
    print("\n--- Lista de Consultas ---")
    print("-" * 125)
    print(f"{'ID':<5} {'Mascota ID':<10} {'Fecha y Hora':<19} {'Motivo':<20} {'Tratamiento':<40} {'Médico':<15} {'Costo':<10}")
    print("-" * 125)
    for c in consultas:
        fecha_formateada = c[2].strftime('%Y-%m-%d %H:%M') if isinstance(c[2], datetime) else str(c[2])
        print(f"{c[0]:<5} {c[1]:<10} {fecha_formateada:<19} {c[3]:<20} {c[4]:<40} {c[5]:<15} {c[6]:<10}")
    print("-" * 125)



def getDatosRegistrarConsulta():
    mascota_id = int(input("ID de la mascota: "))
    fecha = input("Fecha y hora (YYYY-MM-DD HH:MM): ").strip()
    fechaHora = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    motivo = input("Motivo de la consulta: ").strip()
    tratamiento = input("Tratamiento: ").strip()
    medico = input("Nombre del médico: ").strip()
    costo = float(input("Costo: "))

    consulta = Consulta()
    consulta.setMascota_id(mascota_id)
    consulta.setFechaHora(fechaHora)
    consulta.setMotivo(motivo)
    consulta.setTratamiento(tratamiento)
    consulta.setMedico(medico)
    consulta.setCosto(costo)

    return consulta


def getDatosEditarConsulta(lista):
    if not lista:
        print("No hay consultas para editar.")
        return None

    listarConsultas(lista)

    try:
        id_consulta = int(input("ID de la consulta a editar: "))
        mascota_id = int(input("Nuevo ID de la mascota: "))
        fecha = input("Nueva fecha y hora (YYYY-MM-DD HH:MM): ").strip()
        fechaHora = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
        motivo = input("Nuevo motivo de consulta: ").strip()
        tratamiento = input("Nuevo tratamiento indicado: ").strip()
        medico = input("Nuevo nombre del médico: ").strip()
        costo = float(input("Nuevo costo de la consulta: "))

        consulta = Consulta()
        consulta.setId_Consulta(id_consulta)
        consulta.setMascota_id(mascota_id)
        consulta.setFechaHora(fechaHora)
        consulta.setMotivo(motivo)
        consulta.setTratamiento(tratamiento)
        consulta.setMedico(medico)
        consulta.setCosto(costo)

        return consulta

    except ValueError as e:
        print(f"Entrada inválida. Detalle: {e}")
        return None


def getIdEliminarConsulta(lista):
    listarConsultas(lista)
    id = input("ID de la consulta a eliminar: ").strip()
    if not id.isnumeric():
        print("ID inválido.")
        return None
    confirmar = input(f"¿Seguro que deseas eliminar la consulta con ID {id}? (s/n): ").lower()
    return int(id) if confirmar == "s" else None
