class Persona:
    def __init__( self, identidad: str, nombre: str, apellido: str, telefono: str ) -> None:
        self.identidad = identidad
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    def __str__(self) -> str:
        return (
            "{ nombre: " + self.nombre + 
            ", apellido: " + self.apellido + 
            ", identidad: " + self.identidad + 
            ",  telefono: " + self.telefono +
            " }"
        )