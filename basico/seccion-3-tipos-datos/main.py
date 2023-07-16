# Generales
variableNumero: int = 10
variableFloat = 1.567
variableString: str = 'Bryan Ariel Sanchez Anariba'
variableBool = False
print( f'Tipo de dato de variableNumero = { type( variableNumero ) }, valor = { variableNumero }' )
print( f'Tipo de dato de variableString = { type( variableString ) }, valor = { variableString }' )
print( f'Tipo de dato de variableBool = { type( variableBool ) }, valor = { variableBool }' )
print( f'Tipo de dato de variableFloat = { type( variableFloat ) }, valor = { variableFloat }' )

# Manejo de cadenas
miGrupoFavorito = "Metallica"
comentario = "The best favorite group"
print( "The ", miGrupoFavorito.upper(), " is " + comentario.upper() )
numeroUno = "1"
numeroDos = "2"
print( "Concatenacion 1 + 2: " + numeroUno + numeroDos )
print( f"Parseo 1 + 2: { ( int( numeroUno ) + int( numeroDos ) ) }" )

# Tipos Bool
miVariable = 3 > 2
print( f"3 > 2: { miVariable }" )
if miVariable:
    print( "La condicion es verdadera" )
else:
    print( "La condicion es falsa" )

# Entrada de datos por consola
numUno = int( input( "Escriba el primer numero: " ) )
numDos = int( input( "Escriba el segundo numero: " ) )
print( f"{ numUno } + { numDos } = { numUno + numDos }" )