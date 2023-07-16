class Persona:

    def __init__(self, nombre: str, edad: int) -> None:
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        self._edad = edad

    def __str__(self) -> str:
        return f'Class Persona = Nombre: { self._nombre }, Edad: { self._edad }'