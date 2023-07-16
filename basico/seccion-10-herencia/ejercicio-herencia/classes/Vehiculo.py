class Vehiculofc:

    def __init__(self, color: str, ruedas: int) -> None:
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas: int):
        self._ruedas = ruedas

    def __str__(self) -> str:
        return f'Datos Vehiculo = Color: { self._color }, Ruedas: { self._ruedas }'