from classes.Color import Color
from classes.FiguraGeometrica import FiguraGeometrica

class Rectangulo( FiguraGeometrica, Color ):
    
    def __init__(self, ancho: float, alto: float, color: str) -> None:
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calculoArea(self) -> float:
        return self._ancho * self._alto
    
    def __str__(self) -> str:
        return f'{ FiguraGeometrica.__str__(self) }, { Color.__str__(self) }'