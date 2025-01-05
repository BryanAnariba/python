number_one: int = 1
number_two: int = 0;

try:
    print(number_one + number_two)
except TypeError as ex:
    print("Ups: un estas intentando sumar un string", ex)
except Exception as ex:
    print(f'Sometime went wrong: {ex}')
finally:
    print("El codigo que este en el finally siempre se ejecuta")