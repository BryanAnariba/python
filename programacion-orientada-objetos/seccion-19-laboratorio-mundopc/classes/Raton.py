from classes.DispositivoEntrada import DispositivoEntrada
class Raton( DispositivoEntrada ):
    # Metodo static para simular el id
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada) -> None:
        Raton.contador_ratones += 1
        self._idRaton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    @property
    def idRaton(self):
        return self._idRaton
    
    def __str__(self) -> str:
        return f'Id: { self._idRaton }, Marca: { self.marca }, Tipo Entrada: { self.tipo_entrada }'

