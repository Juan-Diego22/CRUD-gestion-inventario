class Mascota(object):
    def __init__(self, id_mascota=None, nombre="", especie="", raza="", edad=0, propietario=""):
        self.__id_mascota = id_mascota
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__propietario = propietario

#Encapsulamiento
    def getId_Mascota(self):
        return self.__id_mascota

    def setId_Mascota(self, id_mascota):
        self.__id_mascota = id_mascota

    def getNombre(self):
        return self.__nombre    

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie 

    def getRaza(self):
        return self.__raza

    def setRaza(self, raza):
        self.__raza = raza

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad 

    def getPropietario(self):
        return self.__propietario

    def setPropietario(self, propietario):
        self.__propietario = propietario 

