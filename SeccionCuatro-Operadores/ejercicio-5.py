"""
    VERIFICAR SI UN PADRE PUEDE VER EL PARTIDO DE SU HIJO
    PARA ELLO DEBE CUMPLIRSE
    QUE EL TENGA VACACIONES O QUE EL TENGA UN DIA DE DESCANSO
"""

# tieneVacaciones: bool = bool( input( "Tienes Vacaciones: " ) )
# tieneUnDiaFeriado: bool = bool( input( "Tienes Un Dia Feriado: " ) )
tieneVacaciones = True
tieneUnDiaFeriado = False

if ( tieneVacaciones or tieneUnDiaFeriado ):
    print( "En efecto hire a ver el juego de mi hijo" )
else:
    print( "En efecto no hire a ver el juego de mi hijo" )