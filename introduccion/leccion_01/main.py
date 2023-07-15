nombre: str = "Bryan Anariba"
print( f"Hola Mundo { nombre }" )

miVariable = "Esta es una variable"
print( miVariable )

miVariable = False
id( miVariable ) # PARA VER SU UBICACION EN MEMORIA
print( "Ubicacion en memoria de la variable con nombre miVariable: ", id( miVariable ) )
print( miVariable )

# Ejercicio, crear tres varoables, para nombre completo, telefono y email e imprimirlas
nombreCompleto: str = "Bryan Ariel Sanchez Anariba"
telefono: str = "504-99999999"
correo: str = "saariel115@gmail.com"

print( f"DATOS PERSONA\n- Nombre Completo: { nombreCompleto }\n- Telefono: { telefono }\n- Correo Electronico: { correo }" )
