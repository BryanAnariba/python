from .Persona import Persona
class Empleado( Persona ):
    def __init__( self, identidad: str, nombre: str, apellido: str, telefono: str, salario: float ) -> None:
        super().__init__( identidad, nombre, apellido, telefono )
        self.salario = salario
