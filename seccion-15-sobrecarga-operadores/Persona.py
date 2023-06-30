class Persona:
    _nombre: str
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def __add__(self, other):
        return f'{self.nombre} - {other.nombre}'
    
    def __sub__(self, other):
        return f'{self.nombre} + {other.nombre}'