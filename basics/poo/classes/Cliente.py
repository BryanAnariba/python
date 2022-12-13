from .Persona import Persona
class Cliente( Persona ):
    def __init__( self, identidad: str, nombre: str, apellido: str, telefono: str, categoria: str ) -> None:
        super().__init__( identidad, nombre, apellido, telefono )
        self.categoria = categoria
