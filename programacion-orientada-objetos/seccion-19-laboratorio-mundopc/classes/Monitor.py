class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio) -> None:
        Monitor.contador_monitores += 1
        self._idMonitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def tamanio(self):
        return self._tamanio
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self) -> str:
        return f'Id: { self._idMonitor }, Marca: { self._marca }, Tamanio: { self._tamanio }'