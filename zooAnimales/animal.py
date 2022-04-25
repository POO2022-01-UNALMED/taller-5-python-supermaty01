class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos : {}\nAves : {}\nReptiles : {}\nPeces : {}\nAnfibios : {}".format(Mamifero.cantidadMamiferos(),
                                                                                            Ave.cantidadAves(),
                                                                                            Reptil.cantidadReptiles(),
                                                                                            Pez.cantidadPeces(),
                                                                                            Anfibio.cantidadAnfibios())

    def toString(self):
        st = "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self._nombre, self._edad, self._habitat,self._genero)
        if self._zona is not None:
            st += ", la zona en la que me ubico es {}, en el {}".format(self._zona.getNombre(), self._zona._zoo.getNombre())
        return st
