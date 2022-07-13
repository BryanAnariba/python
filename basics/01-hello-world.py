# VARIABLES

employeeRole = 'Systems Enginner'
employeeAge = 25
employeeYears = 2
print( 'Role: ' + employeeRole )
print( 'Age: ', employeeYears, ' years' ) # Primera forma para imprimir numeros en print
print( 'Experience: '+ str( employeeYears ) ) # Segunda forma para imprimir numeros en print

nombreUsuario = input( 'Write your name:' )
edadUsuario = int( input( 'Digite su edad: ' ) )
if edadUsuario >= 18 and edadUsuario < 66:
    print( 'Name: ' + nombreUsuario )
    print( 'Congrats, you can to go.' )
else: 
    print( 'Name: ' + nombreUsuario )
    print( 'Sorry you can not tu go.' )

verifyIsParNumber = float( input( 'Write a number: ' ) )
if ( verifyIsParNumber % 2 ) == 0:
    print( "Par Number" )
else: 
    print( "Impar Number" )