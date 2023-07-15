class Persona:

    # Constructor
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Methods || Functions
    def __str__( self ) -> str:
        return '{' + f' nombre: { self._nombre }, apellido: { self._apellido }, edad: { self._edad }' + ' }'

    def mostrarDetalle( self ) -> str:
        return 'Datos del Usuario: {' + f' nombre: { self._nombre }, apellido: { self._apellido }, edad: { self._edad }' + ' }'
    
    # Getters & Setters
    @property
    def nombre( self ):
        return self._nombre

    @nombre.setter
    def nombre( self, nombre: str ):
        self._nombre = nombre

    @property
    def apellido( self ):
        return self._apellido
    
    @apellido.setter
    def apellido( self, apellido: str ):
        self._apellido = apellido
    
    @property
    def edad( self ):
        return self._edad
    
    @edad.setter
    def edad( self, edad: int ):
        self._edad = edad