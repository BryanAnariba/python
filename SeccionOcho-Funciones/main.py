from funciones import saludo, mensajeBienvenida, suma, listarNombres, sumarColeccionNumeros, multiplicaColeccionNumeros

# Funcion normal
saludo()

# Funcion con parametros
print( mensajeBienvenida( 'Bryan Ariel', 'Sanchez Anariba', 3 ) )

# Funcion con parametros por default
print( f'Suma: { suma(15) }')

# Funcion que recibe n parametros
listarNombres( 'Bryan', 'Ariel', 'Daniela', 'Rebeka', 'Erick', 'Suey' )

"""
    EJERCICIO
        Crear una función para sumar los valores recibidos de tipo numérico, 
        utilizando argumentos variables *args como parámetro de la función 
        y regresar como resultado la suma de todos los valores pasados como argumentos.
"""
print( sumarColeccionNumeros( 1,2,3,4,5,6,7,8,9,10 ) )

"""
    EJERCICIO
        Crear una función para multiplicar los valores recibidos de tipo numérico,
        utilizando argumentos variables *args como parámetro de la función
        y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
print( multiplicaColeccionNumeros( 3,3,3 ) )