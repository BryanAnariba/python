operandoA = 3
# Aritmeticos
operandoB = 2

suma = operandoA + operandoB
resta = operandoA - operandoB
multiplicacion = operandoA * operandoB
division = operandoA / operandoB
divisionInt = operandoA // operandoB
modulo = operandoA % operandoB
exponente = operandoA ** operandoB

print( f'Resultado de suma es: { suma }' )
print( f'Resultado de resta es: { resta }' )
print( f'Resultado de multiplicacion es: { multiplicacion }' )
print( f'Resultado de la division es: { division }' )
print( f'Resultado de la division (int) es: { divisionInt }' ) # 3/2 = 1.5 = 1
print( f'Resultado del modulo es: { modulo }' )
print( f'Resultado del exponente es: { exponente }' ) # 3 elevado ala 3 = 9

# Asignacion
miVariable:float = 10

print( miVariable )

miVariable += 1 #Incremento
print( f'Incremento: { miVariable }' )

miVariable -= 1 #Decremento
print( f'Decremento: { miVariable }' )

miVariable *= 3 # 10 * 3
print( f'Producto: { miVariable }' )

miVariable /= 2
print( f'Division: { miVariable }' )

# Comparacion
a = 4
b = 2

aIgualb = ( a == b ) # False
print( f'a es igual que b: { aIgualb }' )

aDiferenteb = ( a != b ) # True 
print( f'a es diferente que b: { aDiferenteb }' )

aMayorb = ( a > b ) # True
print( f'a es mayor que b: { aMayorb }' )

aMenorb = ( a < b ) # False
print( f'a es menor que b: { aMenorb }' )

aMayorIgualb = ( a >= b )
print( f'a es mayor o igual que b: { aMayorIgualb }' )

aMenorIgualb = ( a <= b )
print( f'a es menor o igual que b: { aMenorIgualb }' )

#Logicos
valorA = True
valorB = True

valorAEsIgualvalorB = valorA and valorB
print( f'AND valorAEsIgualvalorB { valorAEsIgualvalorB }' )
valorAEsIgualvalorB = valorA or valorB
print( f'OR valorAEsIgualvalorB { valorAEsIgualvalorB }' )
valorAEsIgualvalorB = not valorA
print( f'NOT valorA negar es igual: { valorAEsIgualvalorB }' )