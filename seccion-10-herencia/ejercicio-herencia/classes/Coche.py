from classes.Vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color: str, ruedas: int, velocidad: float) -> None:
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad: float):
        self._velocidad = velocidad

    def __str__(self) -> str:
        return f'{super().__str__()}, Datos Coche = Velocidad: { self._velocidad }'