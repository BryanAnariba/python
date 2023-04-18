# PEDIR UN VALOR Y VER SI ES VALOR ESTA DENTRO DEL RANGO DE [0,5]

numeroUsuario: float = float( input( 'Escriba un numero para ver si se encuentra dentro del rango: ' ) )

if ( numeroUsuario >= 0 and numeroUsuario <= 5 ):
    print( f'El numero { numeroUsuario } se encuentra dentro del rango' )
else:
    print( f'El numero { numeroUsuario } no se encuentra dentro del rango' )