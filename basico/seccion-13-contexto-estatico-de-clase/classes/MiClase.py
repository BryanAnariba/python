
class MyClase:
    variableClase = 'Valor Variable Clase'

    def __init__(self, variable_instancia) -> None:
        self._variable_instancia = variable_instancia

    # Metodo estatico o funcion estatica
    @staticmethod
    def metodoEstatico():
        print( MyClase.variableClase )

    @classmethod
    def metodoClase(cls):
        print( cls.variableClase )

    def metodoInstanciasMetodoNormalDeClase(self):
        self.metodoEstatico()
        self.metodoClase()
        