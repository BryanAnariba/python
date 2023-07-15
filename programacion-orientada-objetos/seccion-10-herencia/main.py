from classes.Empleado import Empleado
from classes.Persona import Persona

def main():

    nuevaPersona = Persona( 'Erick David', 'Anariba' )
    print( nuevaPersona )

    nuevoEmpleado = Empleado( 'Bryan Ariel', 29, 3500 )
    print( nuevoEmpleado )

main()