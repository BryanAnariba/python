from classes.Persona import Persona

class Empleado(Persona):
    
    def __init__(self, nombre:str, edad: int, sueldo: float) -> None:
        super().__init__( nombre, edad )
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo: float):
        self._sueldo = sueldo

    def __str__(self) -> str:
        return f'{ super().__str__() }, Class Empleado = Sueldo: { self._sueldo }'