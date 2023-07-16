from classes.DispositivoEntrada import DispositivoEntrada

class Teclado( DispositivoEntrada ):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada) -> None:
        Teclado.contador_teclados += 1
        self._idTeclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    @property
    def idTeclado(self):
        return self._idTeclado
    
    def __str__(self) -> str:
        return f'Id: { self._idTeclado }, Marca: { self.marca }, Tipo Entrada: { self.tipo_entrada }'