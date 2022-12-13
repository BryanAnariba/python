from classes.Empleado import Empleado
from classes.Cliente import Cliente

personas: list = []

emp = Empleado( '0801199707000', 'Test 1', 'Test 1', '99999999', 1500.99 )
emp1 = Empleado( '0801199707001', 'Test 1', 'Test 1', '88888888', 1600.99 )
cli = Cliente( '0801199707002', 'Test 3', 'Test 3', '77777777', 'VIP' )
cli1 = Cliente( '0801199707004', 'Test 4', 'Test 4', '66666666', 'PLUS' )

personas.append( emp )
personas.append( emp1 )
personas.append( cli )
personas.append( cli1 )

for persona in personas:
    print( persona )

# print( 'Empleado: ', emp )
# print( 'Cliente: ', cli )
