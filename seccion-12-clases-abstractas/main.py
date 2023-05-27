from classes.Cuadrado import Cuadrado
from classes.Rectangulo import Rectangulo

def main():

    # LOS METODOS ABSTRACTOS DE LA CLASE PADRE DEBEN SER OBLIGATORIO EN LAS CLASES HIJAS, A SU VEZ UN METODO ABSTRACTO HACE LA CLASE ABSTRACTA
    cuadrado = Cuadrado(5, 5, 'Red')
    print( f'Area cuadrado: { cuadrado.calcularArea() }' )
    print( cuadrado )

    rectangulo = Rectangulo(4, 6, 'Gris')
    print( f'Area rectangulo: { rectangulo.calcularArea() }' )
    print(rectangulo)

main()

