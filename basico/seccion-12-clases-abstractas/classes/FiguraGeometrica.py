from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho: float, alto: float) -> None:
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto: float):
        self._alto = alto

    def __str__(self) -> str:
        return f'Datos Figura Geometrica = Alto: { self._alto }, Ancho: { self._ancho }'

    @abstractmethod
    def calcularArea(self):
        pass