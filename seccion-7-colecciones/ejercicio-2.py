# TODO: dada la siguiente tupla, construir una lista que solo contenga los numeros menores a 5
numeros: tuple = ( 13, 1, 8, 3, 2, 5, 8 )
numerosMenoresCinco: list = []

for numero in numeros:
    if numero < 5:
        numerosMenoresCinco.append( numero )

print( 'Lista con numeros menores a cinco' )
print( numerosMenoresCinco )