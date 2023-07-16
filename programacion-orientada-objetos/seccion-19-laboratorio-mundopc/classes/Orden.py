class Orden:

    contador_ordenes = 0

    def __init__(self, listadoComputadoras) -> None:
        Orden.contador_ordenes += 1
        self._idOrden = Orden.contador_ordenes
        self._listadoComputadoras = listadoComputadoras

    @property
    def idOrden(self):
        return self._idOrden
    
    def __str__(self) -> str:
        computadoras_str = ''
        for computadora in self._listadoComputadoras:
            computadoras_str += computadora.__str__()


        return f'''
            Orden: { self._idOrden }
            Listado Computadoras Compradas: { computadoras_str }
        '''