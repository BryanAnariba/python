from classes.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    def __init__(self, color: str, ruedas: int, tipo: str):
        super().__init__( color, ruedas )
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    def __str__(self) -> str:
        return f'{super().__str__()}, Datos Bicicleta = Tipo: { self._tipo }'