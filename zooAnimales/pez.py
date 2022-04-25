from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color, largo):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = color
        self._cantidadAletas = largo
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def setCantidadAletas(self, largo):
        self._cantidadAletas = largo

    @staticmethod
    def movimiento():
        return ""

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)