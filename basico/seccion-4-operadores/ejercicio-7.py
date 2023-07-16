"""
    Instrucciones de tareas:
    Solicitar al usuario dos valores, y determinar cual número es el mayor
    Solicitar al usuario dos valores:
    numero1 (int)
    numero2 (int)
    Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
    Proporciona el numero1:
    Proporciona el numero2:
    El numero mayor es:<numeroMayor>
"""

numeroUno: float = float( input( 'Proporcione el primer numero: ' ) )
numeroDos: float = float( input( 'Proporcione el segundo numero: ' ) )\

if numeroUno > numeroDos:
    print( f'El numero { numeroUno } es mayor que el numero { numeroDos }' )
elif numeroDos > numeroUno:
    print( f'El numero { numeroDos } es mayor que el numero { numeroUno }' )
elif numeroUno == numeroDos:
    print( 'Los numeros son iguales' )
else:
    print( 'No valido' )
