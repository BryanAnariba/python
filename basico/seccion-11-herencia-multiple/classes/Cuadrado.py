from classes.FiguraGeometrica import FiguraGeometrica
from classes.Color import Color

class Cuadrado( FiguraGeometrica, Color ):

    def __init__(self, ancho: float, alto: float, color: str) -> None:
        # En herencia multiple no se usa el super()
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
        

    def calcularAre(self) -> float:
        return self._alto * self._ancho
    
    def __str__(self):
        return f'{ FiguraGeometrica.__str__(self) }, { Color.__str__(self) }'