class Producto:
    contadorProductos: int = 0
    _idProducto: int
    _nombreProducto: str
    _precioProducto: float

    def __init__(self, nombreProducto: str, precioProducto: float) -> None:
        Producto.contadorProductos += 1
        self._idProducto: int = Producto.contadorProductos
        self._nombreProducto: str = nombreProducto
        self._precioProducto: float = precioProducto

    @property
    def nombreProducto(self) -> str:
        return self._nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(self, nombreProducto: str) -> None:
        self._nombreProducto = nombreProducto

    @property
    def precioProducto(self) -> float:
        return self._precioProducto
    
    @precioProducto.setter
    def precioProducto(self, precioProducto: float) -> None:
        self._precioProducto = precioProducto

    def __str__(self) -> str:
        return f'Datos Producto= idProducto: { self._idProducto }, nombreProducto: { self._nombreProducto }, precioProducto: { self._precioProducto }'
