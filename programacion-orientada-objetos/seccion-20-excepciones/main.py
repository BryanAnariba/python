from NumerosIdenticosException import NumerosIdenticosException

resultado = None
try:
    a = int(input('Escriba el primer numero: '))
    b = int(input('Escroba el segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Los numeros son identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: { e }')
except TypeError as e:
    print(f'Ocurrio un error: { e }')
except Exception as e:
    print(f'Ocurrio un error: { e }')
else:
    print('No cayo en ninguna excepcion')
finally:
    print('En finally aunque se entre o no a una excepcion siempre entrara, util para cerrar flujos o conexiones')

print(f'Resultado: resultado')
print('continuamos')