"""
    VERIFICAR SI UN PADRE PUEDE VER EL PARTIDO DE SU HIJO
    PARA ELLO DEBE CUMPLIRSE
    QUE EL TENGA VACACIONES O QUE EL TENGA UN DIA DE DESCANSO

    USE EL OPERADOR NOT
"""

tieneVacaciones: bool = False
tieneFeriado: bool = True

if ( not ( tieneVacaciones or tieneFeriado ) ):
    print( "En efecto no hire a ver el juego de mi hijo" )
else:
    print( "En efecto hire a ver el juego de mi hijo" )
