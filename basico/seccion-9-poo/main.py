from classes.Persona import Persona

usuariosList: list = []

usuarioUno = Persona( 'Bryan Ariel', 'Sanchez Anariba', 26 )
usuarioDos = Persona( 'Erick David', 'Jimenez Anariba', 15 )

usuariosList.append( usuarioUno.mostrarDetalle() )
usuariosList.append( usuarioDos.mostrarDetalle() )

for usuario in usuariosList:
    print( usuario )

# Al eliminar el objeto genera error
# del usuarioUno
# del usuarioDos

print( '\n====> Getters & Setters <====\n' )
# Usando Setter
usuarioDos.nombre = 'Ericka David'
usuarioDos.apellido = 'Lopez Lopez'
usuarioDos.edad = 100

# Usando getters
print( f'Nombre Usuario: { usuarioDos.nombre }, Apellido Usuario: { usuarioDos.apellido }, Edad Usuario: { usuarioDos.edad }' )

# del usuarioUno
# del usuarioDos