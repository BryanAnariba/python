"""
    Ejercicio: Calculadora de Impuestos
    Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
    # Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""
def calculaPagoArticulo( precioArticulo: float, isv: float ):
    totalPagar = precioArticulo + ( precioArticulo * ( isv/100 ) )
    return f'El total a pagar es: { totalPagar }'

def main():
    isv: float = 16
    precioSSSD: float = 1000
    print( calculaPagoArticulo( precioSSSD, isv ) )

main()