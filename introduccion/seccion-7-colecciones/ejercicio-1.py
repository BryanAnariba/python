# ITERAR UN RANGO DE 0 A 10 E IMPRIMIR LOS DIVISIBLES ENTRE 3
print('\n#ITERAR UN RANGO DE 0 A 10 E IMPRIMIR LOS DIVISIBLES ENTRE 3')
for i in range(0, 11):
    if i % 3 == 0 and i != 0:
        print( f'El numero { i } es divisible entre 3' )

# CREAR UN RANGO DE NUMEROS DE 2 A 6 E IMPRIMELOS
print('\nCREAR UN RANGO DE NUMEROS DE 2 A 6 E IMPRIMELOS')
for i in range( 2, 7 ):
    print( i )

# CREAR UN RANGO DE 3 A 10, PERO CON INCREMENTO DE 2 EN 2 EN LUGAR DE 1 EN 1
print( '\nCREAR UN RANGO DE 3 A 10, PERO CON INCREMENTO DE 2 EN 2 EN LUGAR DE 1 EN 1' )
for i in range( 3, 10, 2 ):
    print( f'3 A 10 DE DOS EN DOS: { i }' )

