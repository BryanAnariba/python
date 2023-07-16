from classes.Pelicula import Pelicula

def main():
    opcion: int
    opcion = int(input('PELICULAS APP\n0. Salir\n1. Agregar Pelicula\n2. Listar Peliculas\n3. Eliminar Catalogo de Peliculas\nSeleccione Una opcion: '))
    while opcion != 0:
        if opcion == 1:
            nombre: str = input('Escriba el nombre de la pelicula: ')
            pelicula = Pelicula(nombre)
            pelicula.create()
        elif opcion == 2:    
            pelicula = Pelicula()
            pelicula.find()
        elif opcion == 3:
            pelicula = Pelicula()
            pelicula.removeTxt()
            print('Peliculas Eliminadas con exito')
        elif opcion == 0:
            exit
        else:
            print('Opcion no valida')
        opcion = int(input('PELICULAS APP\n0. Salir\n1. Agregar Pelicula\n2. Listar Peliculas\n3. Eliminar Catalogo de Peliculas\nSeleccione Una opcion: '))


main()