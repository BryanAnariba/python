'''
    ESTACION DEL ANIO EN LA QUE ME ENCUENTRO SEGUN EL MES QUE DIGITO

    primavera (del 20 de marzo al 20 de junio)
    verano (del 21 de junio al 23 de septiembre)
    otoño (del 24 de septiembre al 21 de diciembre)
    invierno (del 22 de diciembre al 19 de marzo)
'''

mesDelAnio: int = int(input( 'Escriba el mes del anio en el que se encuentra (1-12): ' ))
estacion = None

if mesDelAnio == 1 or mesDelAnio == 2 or mesDelAnio == 12:
    estacion = 'Invierno'
elif mesDelAnio == 3 or mesDelAnio == 4 or mesDelAnio == 5:
    estacion = 'Primavera'
elif mesDelAnio == 6 or mesDelAnio == 7 or mesDelAnio == 8:
    estacion = 'Verano'
elif mesDelAnio == 9 or mesDelAnio == 10 or mesDelAnio == 11:
    estacion = 'Otonio'
else:
    estacion = 'Mes proporcionado incorrecto'

print( f'Para el mes { mesDelAnio } la estacion que le corresponde es: { estacion }' )
