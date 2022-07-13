def getEmogis( textoRemplazado ):
    textoRemplazado = textoRemplazado.replace( ':)', '🙂')
    textoRemplazado = textoRemplazado.replace( ':(', '🙃')
    textoRemplazado = textoRemplazado.replace( ':D', '😁')
    return textoRemplazado


texto = input( '>' )
texto = getEmogis( texto )
while texto.find( "adios" ) == -1:
    print( '<' + texto )
    texto = input( '>' )
    texto = getEmogis( texto )

print( "Conversacion finalizada con exito" )