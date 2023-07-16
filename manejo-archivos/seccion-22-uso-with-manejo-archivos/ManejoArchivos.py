class ManejoRecursos:
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self._nombre = open(self._nombre, 'r', encoding='utf8')
        return self._nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self._nombre:
            self._nombre.close()