# Verificar si un numero es par o impar

numero: float = float( input( 'Escriba un numero para verificar si es par o impar: ' ) )

if ( numero % 2 == 0 ):
    print( f'El numero { numero } es par' )
else:
    print( f'El numero { numero } es impar' )