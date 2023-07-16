from classes.Producto import Producto
from classes.Orden import Orden

productos: list = []
def main() -> None:
    pizza = Producto( '1 Pizza Hawaiana', 199.99 )
    pupusas = Producto( '2 Pupusas Con Quesillo', 99.99 )
    limonadas = Producto( '2 Limonadas', 50.99 )
    
    productos.append( pizza )
    productos.append( pupusas )
    productos.append( limonadas )
    nuevaOrden = Orden( productos )
    print(f'=====DETALLE ORDEN:=====\n{nuevaOrden}\n=====TOTAL ORDEN:=====\nL.{ nuevaOrden.calcularTotalPrecioProductos() }')

    productos.clear()

    camisas = Producto( '2 Camisas Polo US', 1000.98 )
    productos.append( camisas )
    nuevaOrdenCamisas = Orden( productos )
    print(f'=====DETALLE ORDEN #2:=====\n{nuevaOrdenCamisas}\n=====TOTAL ORDEN #2:=====\nL.{ nuevaOrdenCamisas.calcularTotalPrecioProductos() }')


main()