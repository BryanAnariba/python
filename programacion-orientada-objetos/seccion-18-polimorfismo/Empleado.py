class Empleado:
    def __init__(self, nombre: str, sueldo: float) -> None:
        self._nombre = nombre
        self._sueldo = sueldo

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def sueldo(self) -> float:
        return self._sueldo
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    @sueldo.setter
    def sueldo(self, sueldo: float) -> None:
        self._sueldo = sueldo

    def __str__(self) -> str:
        return f'Nombre: { self._nombre  }, Sueldo: { self._sueldo }'
        