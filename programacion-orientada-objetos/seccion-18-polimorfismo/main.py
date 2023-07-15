from Empleado import Empleado
from Gerente import Gerente

def imprimeDatosObjeto(objeto):
    print(objeto)
    print(type(objeto))

def main() -> None:
    empleado = Empleado( 'Bryan Ariel', 800.99 )
    imprimeDatosObjeto(empleado)
    gerenteSucursal = Gerente( 'Bryan Ariel Sanchez Anariba', 1000, 'Tecnologia' )
    imprimeDatosObjeto(gerenteSucursal)

main()


