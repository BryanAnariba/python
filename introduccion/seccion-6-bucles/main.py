# While
print( '======= CICLO WHILE ========' )
contador: int = 0
while contador < 3:
    print( f'Contador: { contador }' )
    contador += 1

# For
print( '======= CICLO FOR ========' )
cadena: str = 'HOLA'
for letra in cadena:
    print( f'Letra: { letra }' )

# break => rompe el bucle for y sale de el
print( '======= CICLO FOR CON BREAK ========' )
for letra in 'Holanda':
    if letra == 'a':
        print( f'Letra encontrada { letra }' )
        break

# contiue => no rompe el bucle for, solo salta la linea y sigue el for en ejecucion
print( '======= CICLO FOR CON CONTINUE ========' )
for numero in range( 10 ):
    if numero % 2 == 0:
        print( f'Numero Par Encontrado: { numero }' )
    else:
        continue