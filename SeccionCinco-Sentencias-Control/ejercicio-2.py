'''
    Proporciona tu edad:

    0-10: La infancia es increíble...
    10-20: Muchos cambios y mucho estudio... 
    20-30: Amor y comienza el trabajo...

    Cualquier otro valor: Etapa de vida no reconocida
'''

edadPersona: int = int( input( 'roporciona tu edad: ' ) )
mensaje: str = None

if edadPersona >= 0 and edadPersona < 10:
    mensaje = 'La infancia es increíble...'
elif edadPersona >= 10 and edadPersona < 20:
    mensaje = 'Muchos cambios y mucho estudio... '
elif edadPersona >= 20 and edadPersona < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida no reconocida'

print( f'Tu edad es: { edadPersona } - { mensaje }' )