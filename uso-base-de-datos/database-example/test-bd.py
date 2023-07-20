from services.read import readAll
from services.read_one import readOne
from services.create import create
from services.update import actualizar
from services.delete import eliminar

def main():

    # Crear registro
    create()

    # Todos los datos
    readAll()

    # Un datos
    readOne()

    # Actualizar un registro
    actualizar()

    # Eliminar registro
    eliminar()

main()