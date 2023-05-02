'''CALCULO DE TERMPERATURAS DE FARENTHEIT A CELSIUS Y VICEVERSA'''

def fACelsius( gradosFarenheit = 0 ):
    gradosCelsius: float = ( gradosFarenheit - 32 ) * ( 5/9 )
    return gradosCelsius

def cAFarenheit( gradosCelsius = 0 ):
    gradosFarenheit: float = ( gradosCelsius * ( 9/5 ) ) + 32
    return gradosFarenheit

def main():
    print( "Que desea calcular? " )
    print( "1. Grados Celsius a Farenheit " )
    print( "2. Grados Farenheit a Celsius " )
    opcion: int = int( input( "Digite una opcion: " ) )
    while( opcion != 0 ):
        if opcion == 1:
            gradosCelsius: float = float( input( "Escriba los grados celsius: " ) )
            print( f'{ gradosCelsius } a Franheit son: { cAFarenheit( gradosCelsius ) }' )
        elif opcion == 2:
            gradosFarenheit: float = float( input( "Escriba los grados farenheit: " ) )
            print( f'{ gradosFarenheit } a Celsius son: { fACelsius( gradosFarenheit ) }' )
        else:
            print( "Opcion no valida" )
            exit
        print( "Que desea calcular? " )
        print( "1. Grados Celsius a Farenheit " )
        print( "2. Grados Farenhheit a Celsius " )
        opcion = int( input( "Digite una opcion" ) )

main()

