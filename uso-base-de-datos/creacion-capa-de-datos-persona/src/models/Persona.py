class Persona:
    def __init__(self, idPersona = None, nombrePersona: str = '', apellidoPersona: str = '', emailPersona: str = '') -> None:
        self._idPersona = idPersona
        self._nombrePersona = nombrePersona
        self._apellidoPersona = apellidoPersona
        self._emailPersona = emailPersona

    # Getters
    @property
    def nombrePersona(self) -> str:
        return self._nombrePersona

    @property
    def apellidoPersona(self) -> str:
        return self._apellidoPersona
    
    @property
    def emailPersona(self) -> str:
        return self._emailPersona
    
    @property
    def idPersona(self) -> int:
        return self._idPersona

    # Setters
    @nombrePersona.setter
    def nombrePersona( self, nombrePersona: str ) -> None:
        self._nombrePersona = nombrePersona

    @apellidoPersona.setter
    def apellidoPersona( self, apellidoPersona: str ) -> None:
        self._apellidoPersona = apellidoPersona

    @emailPersona.setter
    def emailPersona( self, emailPersona ) -> None:
        self._emailPersona = emailPersona
    
    @idPersona.setter
    def idPersona( self, idPersona ) -> None:
        self._idPersona = idPersona
    
    def __str__(self) -> str:
        return f'Persona id: { self._idPersona }, nombre: { self._nombrePersona }, apellido: { self._apellidoPersona }, email: { self._emailPersona }'

        