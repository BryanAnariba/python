def encriptar( texto: str ):
    textoFinal: str = ''
    for letra in texto:
        ascii = ord( letra ) # esto retorna el numero ascci de la letra o caracter
        ascii += 1 # caracte en ascci +1
        textoFinal += chr( ascii ) # esto guarda ya el caracter como tal pero como sumamos uno guarda un caracter diferente
    #print( f'Texto Final Encriptado: { textoFinal }' )
    return textoFinal

def decencriptar( texto: str ):
    textoFinal: str = ''
    for letra in texto:
        ascii = ord( letra ) # esto retorna el numero ascci de la letra o caracter
        ascii -= 1 # ahora si restamos el caracter diferernte y muestra el caracter real caracte en ascci - 1
        textoFinal += chr( ascii ) 
        
    #print( f'Texto Final Decencriptar: { textoFinal }' )
    return textoFinal

def encriptarTextoArchivo( rutaArchivo: str ):
    leerArchivo = open( rutaArchivo, 'r' )
    texto = leerArchivo.read()
    leerArchivo.close()
    textoEncriptado = encriptar( texto )

    archivo = open( rutaArchivo, 'w' )
    archivo.write( textoEncriptado )
    archivo.close()

def descencriptarTextoArchivo( rutaArchivo: str ):
    leerArchivo = open( rutaArchivo, 'r' )
    texto = leerArchivo.read()
    leerArchivo.close()
    textoDescencriptado = decencriptar( texto ) #"Hxoxlxax xMxuxnxdxox"

    archivo = open( rutaArchivo, 'w' )
    archivo.write( textoDescencriptado )
    archivo.close()

opcion = input( 'Preciona la letra E para encriptar o D para descencriptar: ' )
rutaArchivo = input( 'Ingrese la ruta del archivo: ' )
if opcion == 'E':
    encriptarTextoArchivo( rutaArchivo )
    print( 'Se encripto correctamente' )
else:
    descencriptarTextoArchivo( rutaArchivo )
    print( 'Se desencripto correctamente' )