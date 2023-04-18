nombreLibro: str = input( 'Proporcione el nombre del libro: ' )
idLibro: int = int( input( 'Proporcione el id del libro: ' ) )
precioLibro: float = float( input( 'Proporcione el precio del libro: ' ) )
envioGratuitoEntrada = input( 'El envio es gratuito (True/False): ' )

if envioGratuitoEntrada == 'True':
    envioGratuito = True
elif envioGratuitoEntrada == 'False':
    envioGratuito = True
else:
    envioGratuito = 'Valor incorrecto'

print( f'Nombre: { nombreLibro }\nCodigo: { idLibro }\nPrecio: { precioLibro }\nEnvio Gratuito?: { envioGratuito }' )