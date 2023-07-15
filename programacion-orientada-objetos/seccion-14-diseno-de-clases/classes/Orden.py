from .Producto import Producto

class Orden:
    contadorOrdenes: int = 0
    _idOrden: int
    _productos: list
    def __init__(self, productos: list) -> None:
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._productos = list( productos )

    @property
    def productos(self) -> list:
        return self._productos
    
    def addProductoAOrden(self, producto: Producto) -> None:
        self._productos.append( producto )
    
    def calcularTotalPrecioProductos(self) -> float:
        total: float = 0
        for producto in self.productos:
            total += producto.precioProducto # ESTO LLAMA AL GETTER DEL PRODUCTO precioProducto
        return total
    
    def __str__(self) -> str:
        productosStr: str = ''
        for producto in self._productos:
            productosStr += producto.__str__() + '|'

        return f'Orden: { self._idOrden }, Productos: { productosStr }'