frutas = [ "Uva", "Manzana", "Pera", "Melon", "Sandia" ]

for fruta in frutas:
    print( "Fruta: " + fruta )
    if fruta.endswith( "a" ) == False:
        print( "Curioso esta fruta no termina en a: " + fruta )

frutas.reverse()
for fruta in frutas:
    print( "Fruta: " + fruta )
    if fruta.endswith( "a" ) == False:
        print( "Curioso esta fruta no termina en a: " + fruta )


frutas.remove( "Uva" )
for fruta in frutas:
    print( "Fruta: " + fruta )
    if fruta.endswith( "a" ) == False:
        print( "Curioso esta fruta no termina en a: " + fruta )

frutas.append( "Kiwi" )
for fruta in frutas:
    print( "Fruta: " + fruta )
    if fruta.endswith( "a" ) == False:
        print( "Curioso esta fruta no termina en a: " + fruta )

texto = "Bryan Ariel Sanchez Anariba"
for letra in texto:
    print( letra )


for numero in range( 10 ):
    if numero > 5:
        print( numero )