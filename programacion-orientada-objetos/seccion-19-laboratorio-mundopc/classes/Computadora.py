class Computadora:
    contador_computadoras = 0
    def __init__(self,nombreComputadora, monitor, teclado, raton) -> None:
        Computadora.contador_computadoras += 1
        self._idComputadora = Computadora.contador_computadoras
        self._nombreComputadora = nombreComputadora
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def idComputadora(self):
        return self._idComputadora
    
    @property
    def nombreComputadora(self):
        return self._nombreComputadora

    @nombreComputadora.setter
    def nombreComputadora(self, nombreComputadora):
        self._nombreComputadora = nombreComputadora

    def __str__(self) -> str:
        return f'''
            Computadora: { self._idComputadora }: { self._nombreComputadora.upper().rstrip().lstrip() }
            Monitor: { self._monitor }
            Teclado: { self._teclado }
            Raton: { self._raton }
        '''
    
