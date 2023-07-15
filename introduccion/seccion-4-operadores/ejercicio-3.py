# Determinar si una persona es mayor de edad

edadPersona: int = int( input( 'Escriba la edad de la persona: ' ) )

if ( edadPersona >= 18 ):
    print( f'Tienes { edadPersona } anios, puedes pasar por que eres maypr de edad' )
else: 
    print( f'Tienes { edadPersona } anios, no puedes pasar por que no es mayor de edad' )