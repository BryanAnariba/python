from Persona import Persona

# Operador de suma puede trabajar de distintas formas => +

#ESTO SE LOGRA MODIFICANDO LOS COMPORTAMIENTOS DE __add__() __sub__() entre otros 

numeroUno: int = 1
numeroDos: int = 2

# aqui el operador + seria suma
numeroTres: int = numeroDos + numeroUno
print(numeroTres)

cadenaUno: str = 'Hola'
cadenaDos: str = 'Mundo'

# aqui seria concatenacion
cadenaTres = cadenaUno + ' ' + cadenaDos
print(cadenaTres)

arregloUno: list = [ 1,2,3 ]
arregloDos: list = [ 4,5,6 ]

# aqui seria union
arregloTres: list = arregloUno + arregloDos
print(arregloTres)

# Pero que pasa con los objetos AQUI AY QUE SMULAR LA CONCATENACION
personaUno = Persona('Bryan')
personaDos = Persona('Ariel')
print(personaUno + personaDos) # add
print(personaUno - personaDos) # sub

