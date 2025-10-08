
class Consulta(object):
    def __init__(self, id_consulta=None, mascota_id=None, fechaHora=None, motivo="", tratamiento="", medico="", costo=0.0):
        self.__id_consulta = id_consulta
        self.__mascota_id = mascota_id
        self.__fechaHora = fechaHora
        self.__motivo = motivo
        self.__tratamiento = tratamiento
        self.__medico = medico
        self.__costo = costo

#Encapsulamiento
    def getId_Consulta(self):
        return self.__id_consulta

    def setId_Consulta(self, id_consulta):
        self.__id_consulta = id_consulta

    def getMascota_id(self):
        return self.__mascota_id 

    def setMascota_id(self, mascota_id):
        self.__mascota_id = mascota_id

    def getFechaHora(self):
        return self.__fechaHora

    def setFechaHora(self, fechaHora):
        self.__fechaHora = fechaHora

    def getMotivo(self):
        return self.__motivo

    def setMotivo(self, motivo):
        self.__motivo = motivo

    def getTratamiento(self):
        return self.__tratamiento

    def setTratamiento(self, tratamiento):
        self.__tratamiento = tratamiento 

    def getMedico(self):
        return self.__medico

    def setMedico(self, medico):
        self.__medico = medico     

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo              