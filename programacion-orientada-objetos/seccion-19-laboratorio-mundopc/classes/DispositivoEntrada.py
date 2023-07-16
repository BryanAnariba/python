class DispositivoEntrada:

    def __init__(self, marca, tipo_entrada) -> None:
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca
    
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    @marca.setter
    def marca( self, marca ):
        self._marca = marca

    @tipo_entrada.setter
    def tipo_entrada( self, tipo_entrada ):
        self._tipo_entrada = tipo_entrada


    def __str__(self) -> str:
        return f'Dispositivo Entrada\n Marca: { self._marca }, Tipo Entrada: { self._tipo_entrada }'