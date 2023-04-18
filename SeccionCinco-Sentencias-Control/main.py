# Conversion numero a string
numero: int = int( input( 'proporciona un numero entre 1 y 3: ' ) )
numeroTexto: str = ''

if numero == 1:
    numeroTexto = 'Numero Uno'
elif numero == 2:
    numeroTexto = 'Numero Dos'
elif numero == 3:
    numeroTexto = 'Numero Tres'
else:
    numeroTexto = 'Numero No Valido Por Que esta fuera de rango'

print( f'Numero proporcionado: { numero } - { numeroTexto }' )

# Ternario
condicion = False
print( 'Se cumple la condicion' ) if condicion else print( 'No se cumple la condicion' )