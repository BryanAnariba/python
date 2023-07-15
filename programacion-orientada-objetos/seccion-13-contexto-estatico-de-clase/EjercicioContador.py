class Persona:
    # Simulando un id con una variable static
    uid: int = 0

    @classmethod
    def _getLastId(cls):
        cls.uid += 1
        return cls.uid
    
    def __init__(self, nombrePersona: str, edadPersona: int) -> None:
        #Persona.uid += 1
        #self.idPersona = Persona.uid
        self.idPersona = Persona._getLastId()
        self._nombrePersona = nombrePersona
        self._edadPersona = edadPersona

    @property
    def nombrePersona(self):
        return self._nombrePersona
    
    @nombrePersona.setter
    def nombrePersona(self, nombrePersona: str):
        self._nombrePersona = nombrePersona

    @property
    def edadPersona(self):
        return self._edadPersona
    
    @edadPersona.setter
    def edadPersona(self, edadPersona: int):
        self._edadPersona = edadPersona

    def __str__(self) -> str:
        return f'Datos Persona: Id: {self.idPersona}, Nombre: {self._nombrePersona}, Edad: {self._edadPersona}'
    

personaUno = Persona( 'Bryan', 26 )
print(personaUno)
personaDos = Persona( 'Ariel', 29 )
print(personaDos)
personaTres = Persona( 'Maria', 25 )
print(personaTres)
print( f'Valor uid: {Persona.uid}' )