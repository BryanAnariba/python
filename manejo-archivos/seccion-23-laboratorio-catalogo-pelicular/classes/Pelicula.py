from classes.PeliculasService import agregarPeliculas, listarPeliculas, eliminarPeliculas

class Pelicula:
    def __init__(self,nombre='') -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self) -> str:
        return f'Nombre: { self._nombre }'
    
    def create(self):
        agregarPeliculas(self._nombre)
    
    def find(self):
        listarPeliculas()

    def removeTxt(self):
        eliminarPeliculas()