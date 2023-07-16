from os import remove, path
ruta_archivo = 'peliculas.txt'

#Server=localhost\SQLEXPRESS02;Database=master;Trusted_Connection=True;

def agregarPeliculas(pelicula):
    if path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf8') as archivo:
            if len(archivo.readlines()) == 0:
                pelicula = pelicula
            else:
                pelicula = '\n' + pelicula
    with open(ruta_archivo, 'a', encoding='utf8') as archivo:
        archivo.write(pelicula)

def listarPeliculas():
    with open(ruta_archivo, 'r', encoding='utf8') as archivo:
        print(archivo.read())

def eliminarPeliculas():
    remove(ruta_archivo)