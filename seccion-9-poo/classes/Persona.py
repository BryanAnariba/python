class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__( self ) -> str:
        return '{' + f' nombre: { self.nombre }, apellido: { self.apellido }, edad: { self.edad }' + ' }'

    def mostrarDetalle( self ) -> str:
        return 'Datos del Usuario: {' + f' nombre: { self.nombre }, apellido: { self.apellido }, edad: { self.edad }' + ' }'