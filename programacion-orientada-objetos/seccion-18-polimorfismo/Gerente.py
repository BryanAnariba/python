from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo: float, departamento: str) -> None:
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    @property
    def departamento(self) -> None:
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: str) -> None:
        self._departamento = departamento

    def __str__(self) -> str:
        return super().__str__() + f', Departamento = { self._departamento }'
    