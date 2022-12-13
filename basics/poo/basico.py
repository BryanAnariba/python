class Cuadrado:
    def __init__(self, ancho: float, largo: float) -> None:
        self.ancho = ancho
        self.largo = largo

    def getArea( self ) -> float:
        return self.ancho * self.largo

figuraUno = Cuadrado( 2.2, 2.2 )
print( f"Area de la figura: { figuraUno.getArea() }" )