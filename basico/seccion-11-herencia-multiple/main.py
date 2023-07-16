from classes.Cuadrado import Cuadrado
from classes.Rectangulo import Rectangulo

def main():
    cuadrado = Cuadrado(5, 5, 'Red')
    print( f'Area cuadrado: { cuadrado.calcularAre() }' )
    print( cuadrado )

    rectangulo = Rectangulo(4, 6, 'Gris')
    print( f'Area cuadrado: { rectangulo.calculoArea() }' )
    print(rectangulo)

