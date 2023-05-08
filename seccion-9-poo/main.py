from classes.Persona import Persona

usuariosList: list = []

usuarioUno = Persona( 'Bryan Ariel', 'Sanchez Anariba', 26 )
usuarioUno.edad = 30
usuarioDos = Persona( 'Erick David', 'Jimenez Anariba', 15 )
usuarioDos.nombre = 'Erickson David'

usuariosList.append( usuarioUno.mostrarDetalle() )
usuariosList.append( usuarioDos )

for usuario in usuariosList:
    print( usuario )